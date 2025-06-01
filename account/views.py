from decimal import Decimal
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import defaultdict
from django.db.models import Sum, F
from django.db.models.functions import TruncDate
from sale.models import *
from .models import *
from .serializers import *
from rest_framework import viewsets
import logging



logger = logging.getLogger(__name__)

@api_view(['GET'])
def income_report_by_day_all_months(request):
    try:
        year = timezone.now().year
        data = defaultdict(lambda: defaultdict(Decimal))

        def aggregate(model, amount_field, label, group_by=None):
            try:

                qs = model.objects.filter(
                    created_at__year=year
                ).annotate(
                    trunc_date=TruncDate('created_at')
                )

                values_fields = ['trunc_date']
                if group_by:
                    values_fields.append(group_by)

                qs = qs.values(*values_fields).annotate(
                    total=Sum(amount_field)
                )

                for item in qs:
                    key = label
                    if group_by:
                        key = item[group_by]
        
                    total = item['total'] if item['total'] is not None else 0
                    data[item['trunc_date']][key] += Decimal(str(total))

            except Exception as e:
                logger.error(f"Error processing {model.__name__}: {str(e)}")
                raise ValueError(f"{label} aggregation failed: {str(e)}")

        # Income from legal services
        aggregate(Vokalatnama, 'total_amount', 'Vokalatnama','sale_type')
        aggregate(Bailbond, 'total_amount', 'Bailbond')
        
        # Associate fees
        aggregate(AssociateRegistration, 'total', 'Associate Registration')
        aggregate(AssociateRenewal, 'renewal_fee', 'Associate Renewal')
        
        # Rent income
        aggregate(RentCollection, 'rent_amount', 'House Rent')
        aggregate(HallRentCollection, 'rent_amount', 'Hall Rent')
        
        # Advocate fees
        aggregate(MonthlyFee, 'total_monthly_amount', 'Monthly Fee')
        aggregate(BarAssociationFee, 'total_amount', 'Bar Association Fee')
        aggregate(EntryFee, 'entry_fee', 'Entry Fee')
        
        # Other income
        aggregate(AdvocateChange, 'fee', 'Advocate Change Fee')
        aggregate(FundCollection, 'fund_amount', 'Donation', 'donation_type')
        aggregate(BillCollection, 'bill_amount', 'Bill Collection')
        aggregate(BankInterest, 'interest_amount', 'Bank Interest')

        # Generate sorted columns and rows
        all_categories = list({k for v in data.values() for k in v.keys()})

        final_rows = [
            {
                'trunc_date': date.strftime('%Y-%m-%d'),
                **{cat: float(data[date].get(cat, 0)) for cat in all_categories},
                'total': float(sum(data[date].values()))  # Daily total
            }
            for date in sorted(data.keys())
        ]

        # Calculate grand totals per category
        category_totals = {
            cat: round(float(sum(row[cat] for row in final_rows if cat in row)), 2)
            for cat in all_categories
        }
        grand_total = sum(category_totals.values())

        return Response({
            'year': year,
            'columns': ['trunc_date'] + all_categories + ['total'],
            'rows': final_rows,
            'category_totals': category_totals,
            'grand_total': round(grand_total, 2)
        })

    except Exception as e:
        logger.exception("Unexpected error in income report")
        return Response({"error": str(e)}, status=500)




class ProbableIncomeViewSet(viewsets.ModelViewSet):
    queryset = ProbableIncome.objects.all()
    serializer_class = ProbableIncomeSerializer



class ProbableExpanseViewSet(viewsets.ModelViewSet):
    queryset = ProbableExpanse.objects.all()
    serializer_class = ProbableExpanseSerializer




