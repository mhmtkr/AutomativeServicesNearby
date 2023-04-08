from flask import Flask, render_template
from places import get_nearby_gas_stations, get_nearby_mechanic_shops, get_nearby_car_washes

import socket
import requests

app = Flask(__name__)

@app.route('/gas-stations')
def show_gas_stations():
    ip_address = get_ip_address()
    location = get_user_location(ip_address)
    radius = 5000  # search radius in meters
    results = get_nearby_gas_stations(location, radius)
    return render_template('results.html', results=results)

@app.route('/mechanic-shops')
def show_mechanic_shops():
    ip_address = get_ip_address()
    location = get_user_location(ip_address)
    radius = 5000  # search radius in meters
    results = get_nearby_mechanic_shops(location, radius)
    return render_template('results.html', results=results)

@app.route('/car-washes')
def show_car_washes():
    ip_address = get_ip_address()
    location = get_user_location(ip_address)
    radius = 5000  # search radius in meters
    results = get_nearby_car_washes(location, radius)
    return render_template('results.html', results=results)

# Retrieve user’s location using HTML5 Geolocation API
#def get_user_location():
#    if 'geolocation' in navigator:
#        navigator.geolocation.getCurrentPosition(
#            lambda position: (position.coords.latitude, position.coords.longitude),
#            lambda error: None
#        )
        
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1)) # Connect to a Google DNS server
    ip_address = s.getsockname()[0]
    return ip_address
    
def get_user_location(ip_address):
#   url = f'https://ipapi.co/{ip_address}/json/'
    url = f'http://ip-api.com/json/{ip_address}'
#   print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        latitude = data['lat']
        longitude = data['lon']
        print(f'Latitude: {latitude}, Longitude: {longitude}')
    else:
        print('Failed to retrieve location')
