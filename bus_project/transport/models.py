from django.db import models

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=100)
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Bus(models.Model):
    name = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=50)
    route =  models.ForeignKey(Route, on_delete=models.CASCADE, related_name='buses')

    def __str__(self):
        return f"{self.name} ({self.bus_number})"
    
class Stop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class RouteStop(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='route_stops')
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = ('route', 'stop')
        ordering = ['order']

    def __str__(self):
        return f"{self.route.name} ({self.route.name})"
    

class Fare(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='fares')
    from_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name= 'fare_from')
    to_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='fare_to')
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('route', 'from_stop', 'to_stop')

    def __str__(self):
        return f"{self.from_stop.name} → {self.to_stop.name}: {self.amount} BDT"