import folium
import phonenumbers
import requests
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

phone_number=input("Enter the number with country code : ")

#Parsing phone number
pn=phonenumbers.parse(phone_number)

#Printing timezone
tz=timezone.time_zones_for_number(pn)
print("Timezone : ",str(tz))

#Printing service provider
sp=carrier.name_for_number(pn,'en')
print("Service Provider : ",str(sp))

#Printing location
location=geocoder.description_for_number(pn,'en')
print("Location : ",str(location))

from opencage.geocoder import OpenCageGeocode
key="fb569aff34bf4f33be144313508dacb9"
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
#print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={key}"

# Send request
response = requests.get(url)
data = response.json()

# Extract address
if data["status"] == "OK":
    address = data["results"][0]["formatted_address"]
    print("Location:", address)
else:
    print("Error:", data["status"])






