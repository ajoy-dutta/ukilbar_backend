from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('person.urls')),
    path('api/', include('sale.urls')),
    path('api/', include('account.urls')),
]
