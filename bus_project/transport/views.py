from django.shortcuts import render
from .models import Route, Stop, Fare

def home(request):
    stops = Stop.objects.all()
    routes = Route.objects.prefetch_related('buses', 'route_stops').all()

    selected_from = None
    selected_to = None
    routes_found = []
    map_stops = []

    from_id = request.GET.get('from_stop')
    to_id = request.GET.get('to_stop')

    if from_id and to_id:
        selected_from = Stop.objects.get(id=from_id)
        selected_to = Stop.objects.get(id=to_id)

        for route in routes:
            route_stops = list(route.route_stops.all())
            stop_ids = [rs.stop.id for rs in route_stops]

            if selected_from.id in stop_ids and selected_to.id in stop_ids:
                from_index = stop_ids.index(selected_from.id)
                to_index = stop_ids.index(selected_to.id)

                if from_index < to_index:
                    relevant_stops = route_stops[from_index:to_index + 1]

                    # 🔥 CLEAR & ADD MAP STOPS
                    map_stops = []
                    for rs in relevant_stops:
                        map_stops.append({
                            "name": rs.stop.name,
                            "lat": rs.stop.latitude,
                            "lng": rs.stop.longitude,
                        })

                    fare = Fare.objects.filter(
                        route=route,
                        from_stop=selected_from,
                        to_stop=selected_to
                    ).first()

                    routes_found.append({
                        "route": route,
                        "fare": fare.amount if fare else "N/A"
                    })

                    break  # ✅ stop after first valid route

    return render(request, "transport/home.html", {
        "stops": stops,
        "routes": routes,
        "routes_found": routes_found,
        "selected_from": selected_from,
        "selected_to": selected_to,
        "map_stops": map_stops
    })
