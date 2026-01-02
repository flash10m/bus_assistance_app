from django.urls import path
from .views import route_list

urlpatterns = [
    path('', route_list, name= 'route_list'),
]