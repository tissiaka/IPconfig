import socket
from ip2geotools.databases.noncommercial import DbIpCity
url = input("Souriez et Entrer une URL : ")
ip = socket.gethostbyname(url)
reponse = DbIpCity.get(ip, api_key = 'free')
print("IP: ", ip)
print("City: ", reponse.city)
print("Region: ", reponse.region)
print("Country: ", reponse.country)
