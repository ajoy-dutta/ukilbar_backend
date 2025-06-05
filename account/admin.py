from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProbableIncome)
admin.site.register(ProbableExpanse)
admin.site.register(ActualExpanse)
admin.site.register(IncomePercentage)
admin.site.register(WelfareFundPercentage)
