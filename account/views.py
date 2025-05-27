# views.py
from rest_framework import viewsets
from .models import ProbableIncome
from .serializers import *



class ProbableIncomeViewSet(viewsets.ModelViewSet):
    queryset = ProbableIncome.objects.all()
    serializer_class = ProbableIncomeSerializer
