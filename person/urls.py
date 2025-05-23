from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='custom-token_obtain_pair'),
    path('advocates/', AdvocateListCreateView.as_view(), name='advocate-list-create'),
    path('advocates/<int:id>/', AdvocateRetrieveUpdateDestroyView.as_view(), name='advocate-detail'),
    path('buildings/', BuildingListCreateView.as_view(), name='building-list-create'),
    path('buildings/<int:id>/', BuildingRetrieveUpdateDestroyView.as_view(), name='building-detail'),
    path('forms/', FormModelListCreateView.as_view(), name='form-list-create'),
    path('forms/<int:id>/', FormModelRetrieveUpdateDestroyView.as_view(), name='form-detail'),
    path('renters/', RenterListCreateView.as_view(), name='renter-list-create'),
    path('renters/<int:id>/', RenterRetrieveUpdateDestroyView.as_view(), name='renter-detail'),
    path('banks/', BankListCreateView.as_view(), name='bank-list-create'),
    path('banks/<int:id>/', BankRetrieveUpdateDestroyView.as_view(), name='bank-detail'),
]
