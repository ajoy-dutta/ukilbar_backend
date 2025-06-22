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





class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['id', 'name', 'gender']



class NomineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nominee
        fields = ['id', 'name', 'address', 'relationship', 'phone', 'birth_year', 'nid', 'birth_certificate']



class AdvocateSerializer(serializers.ModelSerializer):
    children = ChildSerializer(many=True, required=False)
    nominees = NomineeSerializer(many=True, required=False)

    class Meta:
        model = Advocate
        fields = '__all__'

    def create(self, validated_data):
        children_data = validated_data.pop('children', [])
        nominees_data = validated_data.pop('nominees', [])
        advocate = Advocate.objects.create(**validated_data)

        for child in children_data:
            Child.objects.create(advocate=advocate, **child)

        for nominee in nominees_data:
            Nominee.objects.create(advocate=advocate, **nominee)

        return advocate

    def update(self, instance, validated_data):
        children_data = validated_data.pop('children', [])
        nominees_data = validated_data.pop('nominees', [])

        # Update main Advocate fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Optional: Delete and recreate children
        instance.children.all().delete()
        for child in children_data:
            Child.objects.create(advocate=instance, **child)

        # Optional: Delete and recreate nominees
        instance.nominees.all().delete()
        for nominee in nominees_data:
            Nominee.objects.create(advocate=instance, **nominee)

        return instance




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




class PositionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionList
        fields = '__all__' 




class CommitteeMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeMember
        fields = '__all__'