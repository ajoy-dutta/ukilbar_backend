from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view.'})



#Advocate
class AdvocateListCreateView(generics.ListCreateAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer


class AdvocateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    lookup_field = 'id'




#Building
class BuildingListCreateView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class BuildingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    lookup_field = 'id'


#Form
class FormModelListCreateView(generics.ListCreateAPIView):
    queryset = FormModel.objects.all()
    serializer_class = FormModelSerializer

class FormModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormModel.objects.all()
    serializer_class = FormModelSerializer
    lookup_field = 'id'


#Renter
class RenterListCreateView(generics.ListCreateAPIView):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer


class RenterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer
    lookup_field = 'id'




#Bank
class BankListCreateView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    lookup_field = 'id'