import math
import requests

def haversine(lat1, lon1, lat2, lon2):
    # Convert coordinates to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # Calculate difference between latitudes and longitudes
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    # Apply Haversine formula to calculate distance
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    # Radius of the earth in kilometers
    r = 6371
    # Calculate distance in kilometers
    distance = c * r
    return distance

# Coordinates of the two locations
lat1, lon1 = 12.99130015163631, 80.24295478098901
lat2, lon2 = 8.78086525153498, 77.8688078320569

# Call OpenStreetMap API to get coordinates
url = f"https://nominatim.openstreetmap.org/search?q={lat1},{lon1}&format=json"
response = requests.get(url).json()
lat1, lon1 = float(response[0]['lat']), float(response[0]['lon'])

url = f"https://nominatim.openstreetmap.org/search?q={lat2},{lon2}&format=json"
response = requests.get(url).json()
lat2, lon2 = float(response[0]['lat']), float(response[0]['lon'])

# Calculate distance using Haversine formula
distance = haversine(lat1, lon1, lat2, lon2)

print(distance)
