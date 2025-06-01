# serializers.py
from rest_framework import serializers
from .models import *


class ProbableIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProbableIncome
        fields = '__all__'



class ProbableExpanseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProbableExpanse
        fields = '__all__'
