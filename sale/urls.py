from django.urls import path
from .views import *

urlpatterns = [
    
    path('vokalotnama/', vokalotnamaListCreateView.as_view(), name='vokalotnama-list-create'),
    path('vokalotnama/<int:id>/', vokalotnamaRetrieveUpdateDestroyView.as_view(), name='vokalotnama-detail'),

    path('bailbond/', bailBondListCreateView.as_view(), name='bailbond-list-create'),
    path('bailbond/<int:id>/', bailBondRetrieveUpdateDestroyView.as_view(), name='bailbond-detail'),

    path('associate-registration/', AssociateRegistrationListCreateView.as_view(), name='associate-registration-list-create'),
    path('associate-registration/<int:id>/', AssociateRegistrationRetrieveUpdateDeleteView.as_view(), name='associate-registration-detail'),

    path('associate-renewal/', AssociateRenewalListCreateView.as_view(), name='associate-renewal-create'),
    path('associate-renewal/<int:id>/', AssociateRenewalDetailView.as_view(), name='associate-renewal-detail'),

    path('advocate-all-fees/', ConsolidatedFeeView.as_view(), name='advocate-all-fees'),

    path('shop-rent/', HallRentListCreateView.as_view(), name='shop-rent-create'),
    path('shop-rent/<int:id>/', HallRentDetailView.as_view(), name='shop-rent-detail'),

    path('advocate-change/', AdvocateChangeListCreateView.as_view(), name='advocate-change-list-create'),
    path('advocate-change/<int:id>/', AdvocateChangeDetailView.as_view(), name='advocate-change-detail'),


    path('fund-collection/', FundCollectionListCreateAPIView.as_view(), name='fund-collection'),
    path('fund-collection/<int:id>/', FundCollectionDetailView.as_view(), name='fund-collection-detail'),


    path('entry-fees/', EntryFeeListCreateAPIView.as_view(), name='entry-fee-list-create'),
    path('entry-fees/<int:id>/', EntryFeeDetailView.as_view(), name='entry-fee-details'),


    path('electricity-bill/', BillCollectionListCreateAPIView.as_view(), name='electricity-bill-list-create'),
    path('electricity-bill/<int:id>/', BillCollectionDetailView.as_view(), name='electricity-bill-detail'),


    path('bank-interest/', BankInterestListCreateAPIView.as_view(), name='bank-interest-list-create'),
    path('bank-interest/<int:id>/', BankInterestDetailView.as_view(), name='bank-interest-detail'),
    
]
