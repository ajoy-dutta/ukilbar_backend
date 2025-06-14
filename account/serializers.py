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



class ActualExpanseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActualExpanse
        fields = '__all__'



class IncomePercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomePercentage
        fields = '__all__'



class WelfareFundPercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelfareFundPercentage
        fields = '__all__'




class GeneralFundExpanseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralFundExpanseCategory
        fields = '__all__'



class WelfareFundExpanseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WelfareFundExpanseCategory
        fields = '__all__'

