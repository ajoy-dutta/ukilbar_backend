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
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView




logger = logging.getLogger(__name__)

@api_view(['GET'])
def income_report_by_day_all_months(request):
    try:
        year = int(request.GET.get('year', timezone.now().year))
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





# ------------------- Probable Income -------------------
class ProbableIncomeListCreateView(ListCreateAPIView):
    queryset = ProbableIncome.objects.all()
    serializer_class = ProbableIncomeSerializer

    def get_queryset(self):
        year = self.request.query_params.get('year')
        if year and year.isdigit():
            return ProbableIncome.objects.filter(year=year)
        return ProbableIncome.objects.all()



class ProbableIncomeUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ProbableIncome.objects.all()
    serializer_class = ProbableIncomeSerializer
    lookup_field = 'id'




# ------------------- Probable Expanse -------------------
class ProbableExpanseListCreateView(ListCreateAPIView):
    queryset = ProbableExpanse.objects.all()
    serializer_class = ProbableExpanseSerializer

    def get_queryset(self):
        year = self.request.query_params.get('year')
        if year and year.isdigit():
            return ProbableExpanse.objects.filter(year=year)
        return ProbableExpanse.objects.all()



class ProbableExpanseUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ProbableExpanse.objects.all()
    serializer_class = ProbableExpanseSerializer
    lookup_field = 'id'




# ------------------- Actual Expanse -------------------
class ActualExpanseListCreateView(ListCreateAPIView):
    queryset = ActualExpanse.objects.all()
    serializer_class = ActualExpanseSerializer

    def get_queryset(self):
        year = self.request.query_params.get('year')
        if year and year.isdigit():
            return ActualExpanse.objects.filter(year=year)
        return ActualExpanse.objects.all()



class ActualExpanseUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ActualExpanse.objects.all()
    serializer_class = ActualExpanseSerializer
    lookup_field = 'id'






@api_view(['GET'])
def general_income_report(request):
    try:
        year = int(request.GET.get('year', timezone.now().year))
        sales = []

        def collect_entries(model, amount_field, label, extra_fields=None):
            try:
                fields_to_fetch = ['id', amount_field, 'created_at']
                if extra_fields:
                    if isinstance(extra_fields, str):
                      extra_fields = [extra_fields]
                    fields_to_fetch += extra_fields

                print(fields_to_fetch)
                entries = model.objects.filter(created_at__year=year).values(*fields_to_fetch)

                
                for entry in entries:
                    source = entry.get(extra_fields[0]) if extra_fields else label
                    print("entry", entry)
                    record = {
                        'source': source,
                        'id': entry['id'],
                        'amount': float(entry[amount_field]),
                        'date': entry['created_at'].strftime('%Y-%m-%d'),
                    }
                    sales.append(record)

            except Exception as e:
                logger.error(f"Error collecting from {model.__name__}: {str(e)}")

        # Legal service sales
        collect_entries(Vokalatnama, 'total_amount', 'Vokalatnama','sale_type')
        collect_entries(Bailbond, 'total_amount', 'Bailbond')

        # Associate fees
        collect_entries(AssociateRegistration, 'total', 'Associate Registration')
        collect_entries(AssociateRenewal, 'renewal_fee', 'Associate Renewal')

        # Rent
        collect_entries(RentCollection, 'rent_amount', 'House Rent')
        collect_entries(HallRentCollection, 'rent_amount', 'Hall Rent')

        # Advocate fees
        collect_entries(MonthlyFee, 'total_monthly_amount', 'Monthly Fee')
        collect_entries(BarAssociationFee, 'total_amount', 'Bar Association Fee')
        collect_entries(EntryFee, 'entry_fee', 'Entry Fee')

        # Other income
        collect_entries(AdvocateChange, 'fee', 'Advocate Change Fee')
        collect_entries(FundCollection, 'fund_amount', 'Donation', extra_fields=['donation_type'])
        collect_entries(BillCollection, 'bill_amount', 'Bill Collection')
        collect_entries(BankInterest, 'interest_amount', 'Bank Interest')

        # Sort by date (optional)
        sales.sort(key=lambda x: x['date'])

        return Response({
            'year': year,
            'total_records': len(sales),
            'records': sales
        })

    except Exception as e:
        logger.exception("Error generating detailed income report")
        return Response({"error": str(e)}, status=500)






class IncomePercentageListCreateView(ListCreateAPIView):
    queryset = IncomePercentage.objects.all()
    serializer_class = IncomePercentageSerializer


class IncomePercentageUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = IncomePercentage.objects.all()
    serializer_class = IncomePercentageSerializer
    lookup_field = 'id'







class WelfareFundPercentageListCreateView(ListCreateAPIView):
    queryset = WelfareFundPercentage.objects.all()
    serializer_class = WelfareFundPercentageSerializer


class WelfareFundPercentageUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = WelfareFundPercentage.objects.all()
    serializer_class = WelfareFundPercentageSerializer
    lookup_field = 'id'





class GeneralFundExpanseCategoryListCreateView(ListCreateAPIView):
    queryset = GeneralFundExpanseCategory.objects.all()
    serializer_class = GeneralFundExpanseCategorySerializer


class GeneralFundExpanseCategoryDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = GeneralFundExpanseCategory.objects.all()
    serializer_class = GeneralFundExpanseCategorySerializer
    lookup_field = 'id'






class WelfareFundExpanseCategoryListCreateView(ListCreateAPIView):
    queryset = WelfareFundExpanseCategory.objects.all()
    serializer_class = WelfareFundExpanseCategorySerializer


class WelfareFundExpanseCategoryDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = WelfareFundExpanseCategory.objects.all()
    serializer_class = WelfareFundExpanseCategorySerializer
    lookup_field = 'id'





