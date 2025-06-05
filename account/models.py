# models.py
from django.db import models

class ProbableIncome(models.Model):
    IncomeCategory = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    year = models.PositiveIntegerField(blank=True, null = True)

    def __str__(self):
        return self.IncomeCategory
    


class ProbableExpanse(models.Model):
    expanseCategory = models.CharField(max_length=255)
    ProbableExpanse = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null = True)
    year = models.PositiveIntegerField(blank=True, null = True)

    def __str__(self):
        return self.expanseCategory
    



class ActualExpanse(models.Model):
    expanseCategory = models.CharField(max_length=255)
    actualExpanse = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null = True)
    date = models.DateField(blank=True, null = True)
    year = models.PositiveIntegerField(blank=True, null = True)

    def __str__(self):
        return self.expanseCategory



class IncomePercentage(models.Model):
    category = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null = True)
    def __str__(self):
        return self.category-self.percentage


class WelfareFundPercentage(models.Model):
    category = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null = True)
    def __str__(self):
        return self.category-self.percentage
