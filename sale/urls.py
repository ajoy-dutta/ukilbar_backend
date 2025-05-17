from django.urls import path
from .views import *

urlpatterns = [
    
    path('vokalotnama/', vokalotnamaListCreateView.as_view(), name='vokalotnama-list-create'),
    path('vokalotnama/<int:id>/', vokalotnamaRetrieveUpdateDestroyView.as_view(), name='vokalotnama-detail'),

    path('bailbond/', bailBondListCreateView.as_view(), name='bailbond-list-create'),
    path('bailbond/<int:id>/', bailBondRetrieveUpdateDestroyView.as_view(), name='bailbond-detail'),
    
]
