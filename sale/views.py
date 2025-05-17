from django.shortcuts import render
from rest_framework.response import Response
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
