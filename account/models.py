# models.py
from django.db import models

class ProbableIncome(models.Model):
    IncomeCategory = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.title
