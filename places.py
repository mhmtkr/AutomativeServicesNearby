import requests

API_KEY = 'YOUR_API_KEY'
API_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

def get_nearby_gas_stations(location, radius):
    params = {
        'key': API_KEY,
        'location': f'{location[0]},{location[1]}',
        'radius': radius,
        'type': 'gas_station'
    }
    response = requests.get(API_URL, params=params)
    results = response.json()['results']
    return results

def get_nearby_mechanic_shops(location, radius):
    params = {
        'key': API_KEY,
        'location': f'{location[0]},{location[1]}',
        'radius': radius,
        'type': 'car_repair'
    }
    response = requests.get(API_URL, params=params)
    results = response.json()['results']
    return results

def get_nearby_car_washes(location, radius):
    params = {
        'key': API_KEY,
        'location': f'{location[0]},{location[1]}',
        'radius': radius,
        'type': 'car_wash'
    }
    response = requests.get(API_URL, params=params)
    results = response.json()['results']
    return results
