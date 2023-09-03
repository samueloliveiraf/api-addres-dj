from django.contrib import admin
from django.urls import path

from address import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', views.search_address_by_name, name='search-address-by-name'),
]
