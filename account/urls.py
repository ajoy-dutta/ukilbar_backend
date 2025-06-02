# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import * 

# router = DefaultRouter()
# router.register(r'probable_income', ProbableIncomeViewSet)
# router.register(r'probable_expanse', ProbableExpanseViewSet)
# router.register(r'actual_expanse', ActualExpanseViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('income-report/', income_report_by_day_all_months, name='income-report'),

    path('probable_income/', ProbableIncomeListCreateView.as_view()),
    path('probable_income/<int:id>/', ProbableIncomeUpdateDestroyView.as_view()),

    path('probable_expanse/', ProbableExpanseListCreateView.as_view()),
    path('probable_expanse/<int:id>/', ProbableExpanseUpdateDestroyView.as_view()),

    path('actual_expanse/', ActualExpanseListCreateView.as_view()),
    path('actual_expanse/<int:id>/', ActualExpanseUpdateDestroyView.as_view()),
]
