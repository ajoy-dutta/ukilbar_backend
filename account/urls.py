# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProbableIncomeViewSet

router = DefaultRouter()
router.register(r'probabable_income', ProbableIncomeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
