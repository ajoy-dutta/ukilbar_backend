from django.db import models
from person.models import Advocate
from django.utils import timezone



class Vokalatnama(models.Model):
    receipt_no = models.CharField(max_length=255, blank=True, null = True)
    sale_type = models.CharField(max_length=255, blank= True, null = True)
    advocate_name = models.CharField(max_length=50, blank=True, null = True)
    advocateId = models.CharField(max_length=50, blank=True, null = True)
    building_name = models.CharField(max_length=100,blank=True, null = True)
    address = models.TextField(blank=True, null = True)
    sales_date = models.DateField(blank=True, null = True)

    customer_phone = models.CharField(max_length=20, blank=True, null = True)
    customer_name = models.CharField(max_length=100, blank=True, null = True)
    customer_address = models.TextField(blank=True, null = True)

    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null = True)
    total_count = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now, blank=True)


    def __str__(self):
        return f"Receipt #{self.receipt_no} - {self.customer_name}"




class VokalatnamaSerial(models.Model):
    sale = models.ForeignKey(Vokalatnama, related_name='serials', on_delete=models.CASCADE)
    from_serial = models.IntegerField()
    to_serial = models.IntegerField()
    total = models.IntegerField()


    def __str__(self):
        return f"Serial {self.from_serial} to {self.to_serial}"
    


class Bailbond(models.Model):
    receipt_no = models.CharField(max_length=255, blank=True, null = True)
    building_name = models.CharField(max_length=100,blank=True, null = True)
    sales_date = models.DateField(blank=True, null = True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null = True)
    total_count = models.IntegerField(blank=True, null = True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null = True)
    remarks = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)


    def __str__(self):
        return f"Receipt #{self.receipt_no}"
    

class BailbondSerial(models.Model):
    sale = models.ForeignKey(Bailbond, related_name='bailbond_serials', on_delete=models.CASCADE)
    from_serial = models.IntegerField()
    to_serial = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f"Serial {self.from_serial} to {self.to_serial}"
    



class AssociateRegistration(models.Model):
    receipt_no = models.CharField(max_length=100, blank=True)
    registration_date = models.DateField()
    license_no = models.CharField(max_length=100, blank=True, null = True)
    name = models.CharField(max_length=255, blank=True, null = True)
    advocate_name = models.CharField(max_length=255)
    advocate_id = models.CharField(max_length=100)
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    book_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remarks = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        self.total = self.entry_fee + self.book_rate 
        super().save(*args, **kwargs)



class AssociateRenewal(models.Model):
    receipt_no = models.CharField(max_length=100, blank=True)
    associate = models.ForeignKey(AssociateRegistration, on_delete=models.CASCADE, related_name='renewals')
    renewal_date = models.DateField()
    renewal_end_date = models.DateField()
    renewal_fee = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now, blank=True)




class RentCollection(models.Model):
    collection_date = models.DateField()
    advocate_id = models.CharField(max_length=20)
    
    rent_type = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    year = models.PositiveIntegerField(blank=True, null = True)
    building_name = models.CharField(max_length=255)
    floor = models.CharField(max_length=50, blank=True, null = True)
    room = models.CharField(max_length=50, blank=True, null = True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50, blank=True, null = True)
    remarks1 = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.rent_type} Rent - {self.month} {self.year} - {self.advocate_id}"
    


class HallRentCollection(models.Model):
    receipt_no = models.CharField(max_length=20, blank=True, null=True)
    collection_date = models.DateField()
    renter_name = models.CharField(max_length=20)
    from_year = models.PositiveIntegerField(blank=True, null = True)
    from_month = models.CharField(max_length=20)
    to_year = models.PositiveIntegerField(blank=True, null = True)
    to_month = models.CharField(max_length=20)
    building_name = models.CharField(max_length=255)
    floor = models.CharField(max_length=50, blank=True, null = True)
    room = models.CharField(max_length=50, blank=True, null = True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50, blank=True, null = True)
    remarks1 = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.renter_name} Rent - {self.from_month} {self.from_year}"





class MonthlyFee(models.Model):
    collection_date = models.DateField()
    advocate_id = models.CharField(max_length=20)

    from_month = models.IntegerField(blank=True, null = True)
    from_year = models.IntegerField(blank=True, null = True)
    to_month = models.IntegerField(blank=True, null = True)
    to_year = models.IntegerField(blank=True, null = True)
    monthly_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_monthly_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monthly_payment_type = models.CharField(max_length=50)  
    remarks2 = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"Monthly Fee - {self.advocate_id} ({self.from_month}/{self.from_year} to {self.to_month}/{self.to_year})"
    



class BarAssociationFee(models.Model):
    collection_date = models.DateField()
    advocate_id = models.CharField(max_length=20)

    yearly_from_year = models.IntegerField(blank=True, null = True)
    yearly_to_year = models.IntegerField(blank=True, null = True)
    yearly_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    yearly_delay_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    benevolent_fund_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    benevolent_delay_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    relief_fund_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    court_type = models.CharField(max_length=100) 
    remarks3 = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"Bar Association Fee - {self.advocate_id} ({self.yearly_from_year} to {self.yearly_to_year})"



class AdvocateChange(models.Model):
    receipt_no = models.CharField(max_length=10, unique=True, blank=True)
    date = models.DateField(default=timezone.now)
    client_name = models.CharField(max_length=255)
    advocate_id = models.CharField(max_length=100)
    advocate_name = models.CharField(max_length=255)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    case_no = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)


    def save(self, *args, **kwargs):
        if not self.receipt_no:
            prefix = "acf"
            last_entry = AdvocateChange.objects.filter(receipt_no__startswith=prefix).order_by('-id').first()
            if last_entry:
                last_number = int(last_entry.receipt_no[len(prefix):])
                new_number = str(last_number + 1).zfill(6)
            else:
                new_number = "000001"
            self.receipt_no = f"{prefix}{new_number}"
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.receipt_no} - {self.client_name}"
    




class FundCollection(models.Model):
    donation_type = models.CharField(max_length=50)
    receipt_no = models.CharField(max_length=100, unique=True,blank=True)
    date = models.DateField()
    fund_provider = models.CharField(max_length=255)
    fund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=10)
    remarks = models.TextField(blank=True, null=True)
    purpose = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, blank=True)


    def save(self, *args, **kwargs):
        if not self.receipt_no:
            prefix = "f"
            last_entry = FundCollection.objects.filter(receipt_no__startswith=prefix).order_by('-id').first()
            if last_entry:
                last_number = int(last_entry.receipt_no[len(prefix):])
                new_number = str(last_number + 1).zfill(6)
            else:
                new_number = "000001"
            self.receipt_no = f"{prefix}{new_number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.receipt_no} - {self.fund_provider}"
    



class EntryFee(models.Model):
    advocate_id = models.CharField(max_length=20)
    collection_date = models.DateField()
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2)
    remarks4 = models.TextField(blank=True, null=True)
    receipt_no = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    

    def save(self, *args, **kwargs):
        if not self.receipt_no:
            prefix = "EF"
            last_entry = EntryFee.objects.filter(receipt_no__startswith=prefix).order_by('-id').first()
            if last_entry:
                last_number = int(last_entry.receipt_no[len(prefix):])
                new_number = str(last_number + 1).zfill(6)
            else:
                new_number = "000001"
            self.receipt_no = f"{prefix}{new_number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Entry Fee for Advocate {self.advocate_id} on {self.collection_date}"





class BillCollection(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('cash', 'Cash'),
        ('check', 'Check'),
    ]

    receipt_no = models.CharField(max_length=50, unique=True, blank=True)
    collection_date = models.DateField()
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    building_name = models.CharField(max_length=100)
    bill_payer_name = models.CharField(max_length=100)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICES, default='cash')
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)


    def save(self, *args, **kwargs):
        if not self.receipt_no:
            last = BillCollection.objects.order_by('-id').first()
            if last and last.receipt_no.startswith('ECB'):
                last_number = int(last.receipt_no[4:])
                self.receipt_no = f'ECB{last_number + 1:04d}'
            else:
                self.receipt_no = 'ECB0001'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.receipt_no} - {self.bill_payer_name}"
    



class BankInterest(models.Model):
    receipt_no = models.CharField(max_length=50, unique=True, blank=True)
    collection_date = models.DateField()
    bank_name = models.CharField(max_length=40)
    branch_name = models.CharField(max_length=40)
    account_no = models.CharField(max_length=100)
    interest_amount = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)


    def save(self, *args, **kwargs):
        if not self.receipt_no:
            last = BankInterest.objects.order_by('-id').first()
            if last and last.receipt_no.startswith('BI'):
                last_number = int(last.receipt_no[4:])
                self.receipt_no = f'BI{last_number + 1:04d}'
            else:
                self.receipt_no = 'BI0001'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.receipt_no} - {self.bank_name}"

