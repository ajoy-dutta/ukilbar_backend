from django.db import models
from person.models import Advocate



class Vokalatnama(models.Model):
    receipt_no = models.CharField(max_length=255, blank=True, null = True)
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
