from django.urls import path
from .views import home


urlpatterns = [
    path('', home, name='home'),
]

"""from .views import route_list, route_search

urlpatterns = [
    path('', route_list, name= 'route_list'),
    path('search/', route_search, name= 'route_search'),
]"""