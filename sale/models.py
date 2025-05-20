from django.db import models
from person.models import Advocate



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


    def __str__(self):
        return f"Receipt #{self.receipt_no}"
    

class BailbondSerial(models.Model):
    sale = models.ForeignKey(Bailbond, related_name='bailbond_serials', on_delete=models.CASCADE)
    from_serial = models.IntegerField()
    to_serial = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f"Serial {self.from_serial} to {self.to_serial}"
    



class AssociateRenewal(models.Model):
    receipt_no = models.CharField(max_length=100, blank=True)
    renewal_date = models.DateField()
    license_no = models.CharField(max_length=100, blank=True, null = True)
    name = models.CharField(max_length=255, blank=True, null = True)
    year = models.IntegerField()
    advocate_name = models.CharField(max_length=255)
    advocate_id = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[("New", "New"), ("Old", "Old")],blank=True, null = True)
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    book_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    renewal_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remarks = models.TextField(blank=True, null = True)

    def save(self, *args, **kwargs):
        self.total = self.entry_fee + self.book_rate + self.renewal_fee
        super().save(*args, **kwargs)





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

    def __str__(self):
        return f"{self.rent_type} Rent - {self.month} {self.year} - {self.advocate_id}"



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

    def __str__(self):
        return f"Bar Association Fee - {self.advocate_id} ({self.yearly_from_year} to {self.yearly_to_year})"
