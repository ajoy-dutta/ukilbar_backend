from django.db import models
from person.models import Advocate



class Vokalatnama(models.Model):
    receipt_no = models.CharField(max_length=255, blank=True, null = True)
    advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE, related_name='advocate')
    advocateId = models.CharField(max_length=50)
    building_name = models.CharField(max_length=100)
    address = models.TextField()
    sales_date = models.DateField()

    customer_phone = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
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