from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'is_staff': self.user.is_staff,
        }
        return data




class AdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'



class FormModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormModel
        fields = '__all__'




class RenterSerializer(serializers.ModelSerializer):
    building_name = serializers.CharField(source='building_name.building_name', read_only=True)
    class Meta:
        model = Renter
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'



class ExpanseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpanseCategory
        fields = '__all__'



class IncomeCategorySerializer(serializers.ModelSerializer):
     class Meta:
        model = IncomeCategory
        fields = '__all__'

class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = '__all__' 