from django.shortcuts import render

# Create your views here.
from .models import Route

def route_list(request):
    routes = Route.objects.prefetch_related()
    return render(request, 'transport/route_list.html', {'routes': routes})