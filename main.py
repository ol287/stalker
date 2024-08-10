import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
    
def calculate_distance(ip1, ip2):
    res1 = DbIpCity.get(ip1)
    res2 = DbIpCity.get(ip2)
    lat1, lon1 = res1.latitude, res1.longitude
    lat2, lon2 = res2.latitude, res2.longitude
    return distance((lat1, lon1), (lat2, lon2)).km

def get_distance_from_location(ip, lat, lon):
    res = DbIpCity.get(ip)
    ip_lat, ip_lon = res.latitude, res.longitude
    return distance((ip_lat, ip_lon), (lat, lon)).km

def calculate_distance_from_server():
    server_ip = input("Server's IP: ")
    lat = float(input("Your Latitude: "))
    lng = float(input("Your Longitude: "))

    dist = get_distance_from_location(server_ip, lat, lng)
    print(f"Distance between the server and your location is {dist} km")

# Call the function
calculate_distance_from_server()

#ip to geo
ip_add = input("Enter IP: ")  # 198.35.26.96
printDetails(ip_add)


#url to geo 
url = input("Enter URL: ")  # www.youtube.com
ip_add = socket.gethostbyname(url)
printDetails(ip_add)