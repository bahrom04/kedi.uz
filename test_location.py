# key = "AIzaSyBrGSXui1y7HIvTFI0pvFRHNI-zmBZ49H0"


import requests

# def get_coordinates_from_google_maps_url(google_maps_url):
#     # Extract the place ID from the Google Maps URL
#     place_id_index = google_maps_url.find("/place/") + len("/place/")
#     place_id = google_maps_url[place_id_index:].split("/")[0]
#     print(place_id)
#     # Construct the Geocoding API URL
#     geocoding_api_url = f"https://maps.googleapis.com/maps/api/geocode/json?place_id={place_id}&key={key}"

#     # Send a request to the Geocoding API
#     response = requests.get(geocoding_api_url)
#     data = response.json()

#     # Extract latitude and longitude from the response
#     if data['status'] == 'OK':
#         location = data['results'][0]['geometry']['location']
#         latitude = location['lat']
#         longitude = location['lng']
#         return latitude, longitude
#     else:
#         print("Error:", data['status'])
#         return None, None

# # Example usage:
# google_maps_url = "https://maps.app.goo.gl/C4TkmpRL5HToBugb9"
# latitude, longitude = get_coordinates_from_google_maps_url(google_maps_url)
# print("Latitude:", latitude)
# print("Longitude:", longitude)

