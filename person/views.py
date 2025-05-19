from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework import status
from rest_framework import generics
from .models import Advocate


#user
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


#Advocate
class AdvocateListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer


class AdvocateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    lookup_field = 'id'




#Building
class BuildingListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer



class BuildingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    lookup_field = 'id'


#Form
class FormModelListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FormModel.objects.all()
    serializer_class = FormModelSerializer



class FormModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FormModel.objects.all()
    serializer_class = FormModelSerializer
    lookup_field = 'id'


#Renter
class RenterListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer



class RenterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer
    lookup_field = 'id'




#Bank
class BankListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Bank.objects.all()
    serializer_class = BankSerializer



class BankRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    lookup_field = 'id'