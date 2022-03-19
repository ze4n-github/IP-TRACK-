import requests
import json
import os
import time
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
BLACK = '\033[30m'
os.system("clear")
print(RED+"██╗██████╗░  ████████╗██████╗░░█████╗░░█████╗░██╗░░██╗")
print("██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝")
print("██║██████╔╝  ░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░")
print("██║██╔═══╝░  ░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░")
print("██║██║░░░░░  ░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗")
print("╚═╝╚═╝░░░░░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝\n \n")
time.sleep(1)
print(YELLOW+"--------------------------------------")
time.sleep(1)
print("Autor    : ZE4N")
time.sleep(1)
print("--------------------------------------")

time.sleep(1)
print("INSTAGRAM: ze4n.py")
time.sleep(1)
print("--------------------------------------")
time.sleep(1)
print("TIK TOK  : zean.py")
time.sleep(1)
print("-------------------------------------- \n")

api_url = "http://ip-api.com/json/"
parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
data = {"fields":parametros}

def ip_scraping(ip=""):
 res = requests.get(api_url+ip, data=data)
 api_json_res = json.loads(res.content)
 return api_json_res

if __name__ == '__main__':
 ip = input(CYAN+"Ingrese la dirección IP: "+GREEN)


par = parametros.split(",")
for x in par:
 print(x.upper(), ":")
 print( ip_scraping(ip)[x])
 print("===================================")
