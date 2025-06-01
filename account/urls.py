# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import * 

router = DefaultRouter()
router.register(r'probable_income', ProbableIncomeViewSet)
router.register(r'probable_expanse', ProbableExpanseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('income-report/', income_report_by_day_all_months, name='income-report'),
]
