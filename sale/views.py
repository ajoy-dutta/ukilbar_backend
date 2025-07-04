from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework import generics




class vokalotnamaListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vokalatnama.objects.all().order_by('-id')
    serializer_class = VokalatnamaSalesSerializer


class vokalotnamaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vokalatnama.objects.all()
    serializer_class = VokalatnamaSalesSerializer
    lookup_field = 'id'






class bailBondListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Bailbond.objects.all().order_by('-id')
    serializer_class = BailbondSalesSerializer


class bailBondRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Bailbond.objects.all()
    serializer_class = BailbondSalesSerializer
    lookup_field = 'id'






class FormListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FormSale.objects.all().order_by('-id')
    serializer_class = FormSaleSerializer


class FormRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FormSale.objects.all()
    serializer_class = FormSaleSerializer
    lookup_field = 'id'





class AssociateRegistrationListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AssociateRegistration.objects.all().order_by('-registration_date')
    serializer_class = AssociateRegistrationSerializer


class AssociateRegistrationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AssociateRegistration.objects.all()
    serializer_class = AssociateRegistrationSerializer
    lookup_field = 'id'





class AssociateRenewalListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AssociateRenewal.objects.all()
    serializer_class = AssociateRenewalSerializer


class AssociateRenewalDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AssociateRenewal.objects.all()
    serializer_class = AssociateRenewalSerializer
    lookup_field = 'id' 





class AdvocateAllFeeListView(APIView):
    def get(self, request):
        records = AdvocateAllFee.objects.all().order_by('-id')
        serializer = AdvocateAllFeeSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvocateAllFeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)




class AdvocateAllFeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdvocateAllFee.objects.all()
    serializer_class = AdvocateAllFeeSerializer
    lookup_field = 'pk'



class HallRentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = HallRentCollection.objects.all()
    serializer_class = HallRentSerializer


class HallRentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = HallRentCollection.objects.all()
    serializer_class = HallRentSerializer
    lookup_field = 'id' 





class AdvocateChangeListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AdvocateChange.objects.all().order_by('-date')
    serializer_class = AdvocateChangeSerializer


class AdvocateChangeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AdvocateChange.objects.all()
    serializer_class = AdvocateChangeSerializer
    lookup_field = 'id' 






class FundCollectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = FundCollection.objects.all()
    serializer_class = FundCollectionSerializer


class FundCollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FundCollection.objects.all()
    serializer_class = FundCollectionSerializer
    lookup_field = 'id' 





class EntryFeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = EntryFee.objects.all()
    serializer_class = EntryFeeSerializer


class EntryFeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EntryFee.objects.all()
    serializer_class = EntryFeeSerializer
    lookup_field = 'id'





class BillCollectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = BillCollection.objects.all().order_by('-collection_date')
    serializer_class = BillCollectionSerializer


class BillCollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillCollection.objects.all()
    serializer_class = BillCollectionSerializer
    lookup_field = 'id'




class BankInterestListCreateAPIView(generics.ListCreateAPIView):
    queryset = BankInterest.objects.all().order_by('-collection_date')
    serializer_class = BankInterestSerializer


class BankInterestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankInterest.objects.all()
    serializer_class = BankInterestSerializer
    lookup_field = 'id'
