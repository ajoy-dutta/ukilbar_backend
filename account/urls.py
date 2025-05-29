# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProbableIncomeViewSet, income_report_by_day_all_months  

router = DefaultRouter()
router.register(r'probabable_income', ProbableIncomeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('income-report/', income_report_by_day_all_months, name='income-report'),
]
