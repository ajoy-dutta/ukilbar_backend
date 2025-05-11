from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    
    path('vokalotnama/', vokalotnamaListCreateView.as_view(), name='vokalotnama-list-create'),
    path('vokalotnama/<int:id>/', vokalotnamaRetrieveUpdateDestroyView.as_view(), name='vokalotnama-detail'),
    
]
