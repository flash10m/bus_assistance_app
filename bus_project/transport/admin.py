from django.contrib import admin

# Register your models here.
from .models import Route, Bus, Stop, RouteStop, Fare

admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(Stop)
admin.site.register(RouteStop)
admin.site.register(Fare)