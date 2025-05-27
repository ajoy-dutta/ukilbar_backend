# serializers.py
from rest_framework import serializers
from .models import ProbableIncome

class ProbableIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProbableIncome
        fields = '__all__'
