from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework import generics
import requests
from person.models import Advocate





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



    def perform_create(self, serializer):
        advocate_change = serializer.save()

        self.send_sms_to_advocate(advocate_change)

    def send_sms_to_advocate(self, advocate_change):
        case_no = advocate_change.case_no
        advocate_id = advocate_change.advocate_id
        client_name = advocate_change.client_name
        amount = advocate_change.fee

        try:
            advocate = Advocate.objects.get(bar_registration_number=advocate_id)
            phone = advocate.phone
        except Advocate.DoesNotExist:
            print(f"Advocate with ID {advocate_id} not found.")
            return

        if phone:
            message = (
                f"Dear {advocate.name_english}, the case ({case_no}) of client "
                f"{client_name} has been reassigned from you. "
                f"Change fee: {amount} BDT. Thank you for your service."
            )

            try:
                response = requests.post(
                    "http://bulksmsbd.net/api/smsapi?",
                    data={
                        "api_key": "4EsPc8GQcKlWkHoiqvcC",
                        "senderid": "8809617622419",
                        "number": phone,
                        "message": message
                    }
                )
                
                if response.status_code != 200:
                    print(f"SMS API error: {response.text}")

            except requests.RequestException as e:
                print(f"Failed to send SMS: {e}")


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
