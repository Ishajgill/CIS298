from django.shortcuts import render
import requests
from .models import Search

def home(request):
    api_key = 'e0b73ce79fb45e31b85472ff8a7150b0'

    departure = request.GET.get('departure')
    arrival = request.GET.get('arrival')
    flight_number = request.GET.get('flight_number')
    airline = request.GET.get('airline')

    flights = []

    if departure or arrival or flight_number or airline:
        # Save the search to the database
        Search.objects.create(
            departure=departure,
            arrival=arrival,
            flight_number=flight_number,
            airline=airline
        )

        # Fetch flights from API
        url = f'http://api.aviationstack.com/v1/flights?access_key={api_key}'
        if departure:
            url += f'&dep_iata={departure}'
        if arrival:
            url += f'&arr_iata={arrival}'
        if flight_number:
            url += f'&flight_iata={flight_number}'
        if airline:
            url += f'&airline_name={airline}'

        response = requests.get(url)
        data = response.json()

        if 'data' in data:
            flights = data['data']

    # Fetch recent searches (last 5)
    recent_searches = Search.objects.all().order_by('-searched_at')[:5]

    context = {
        'departure': departure,
        'arrival': arrival,
        'flight_number': flight_number,
        'airline': airline,
        'flights': flights,
        'recent_searches': recent_searches
    }
    return render(request, 'flightapp/home.html', context)
