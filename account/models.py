# models.py
from django.db import models

class ProbableIncome(models.Model):
    IncomeCategory = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.IncomeCategory
    


class ProbableExpanse(models.Model):
    expanseCategory = models.CharField(max_length=255)
    ProbableExpanse = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null = True)
    expanse = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null = True)

    def __str__(self):
        return self.expanseCategory
