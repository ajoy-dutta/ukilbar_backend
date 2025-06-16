from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='custom-token_obtain_pair'),
    path('advocates/', AdvocateListCreateView.as_view(), name='advocate-list-create'),
    path('advocates/<int:id>/', AdvocateRetrieveUpdateDestroyView.as_view(), name='advocate-detail'),
    path('buildings/', BuildingListCreateView.as_view(), name='building-list-create'),
    path('buildings/<int:id>/', BuildingRetrieveUpdateDestroyView.as_view(), name='building-detail'),
    path('form/', FormModelListCreateView.as_view(), name='form-list-create'),
    path('form/<int:id>/', FormModelRetrieveUpdateDestroyView.as_view(), name='form-detail'),
    path('renters/', RenterListCreateView.as_view(), name='renter-list-create'),
    path('renters/<int:id>/', RenterRetrieveUpdateDestroyView.as_view(), name='renter-detail'),
    path('banks/', BankListCreateView.as_view(), name='bank-list-create'),
    path('banks/<int:id>/', BankRetrieveUpdateDestroyView.as_view(), name='bank-detail'),

    path('expanse_category/', ExpanseCategoryListCreateView.as_view(), name='expanse_category-list'),
    path('expanse_category/<int:id>/', ExpanseCategoryRetrieveUpdateDestroyView.as_view(), name='expanse_category-detail'),

    path('income_category/', IncomeCategoryListCreateView.as_view(), name='income-category-list'),
    path('income_category/<int:id>/', IncomeCategoryRetrieveUpdateDestroyView.as_view(), name='income-category-detail'),
    
    path('gallery/', PhotoGalleryListCreateView.as_view(), name='gallery-list-create'),
    path('gallery/<int:pk>/', PhotoGalleryDetailView.as_view(), name='gallery-detail'),
]
