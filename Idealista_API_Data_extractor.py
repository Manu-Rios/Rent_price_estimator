# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 16:48:00 2023

@author: riosmanuel.07@gmail.com
"""

import requests

#Credentials need to be encoded in base64-encoding, but that´s done automatically by the 'requests' library
credentials = ("ty1dehiuqxmr33qvqdctkbzptzfalq9w","3VuvxaQszHn9") #API key & Secret

url = "https://api.idealista.com/3.5/es/search"

headers = {
    "Content-Type" : "multipart/form-data"
    }

# params = {
#     "country" : "es",
#     "operation" : "rent",
#     "propertyType" : "homes",
#     "locale" : "es",
#     "maxItems" : "20",
#     "numPage" : "1",
#     "center" : "40.408, -3.700",
#     "distance" : "20"
#     }

params = {
    "country":"es",
    "maxItems":"20",
    "numPage":"1",
    "operation":"rent", #
    "propertyType":"homes", #
    "locationId":"0-EU-ES-28"
    
    
    }


response = requests.post(url, headers = headers, auth = credentials, params = params)

print(f"Response status is {response.status_code}")
print(f"Response status description {response.text}")