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

    path('hall-rent/', HallRentListCreateView.as_view(), name='hall-rent-create'),
    path('hall-rent/<int:id>/', HallRentDetailView.as_view(), name='hall-rent-detail'),
    
]
