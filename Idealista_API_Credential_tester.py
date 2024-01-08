# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:47:23 2024

@author: riosmanuel.07@gmail.com
"""

import requests

#Request to test the credentials

#Credentials need to be encoded in base64-encoding, but that´s done automatically by the 'requests' library
credentials = ("ty1dehiuqxmr33qvqdctkbzptzfalq9w","3VuvxaQszHn9") #API key & Secret

url = "https://api.idealista.com/oauth/token"

#Define the header for the request
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
    }

params = {
        "grant_type": "client_credentials",
        "scope": "read"}

response = requests.post(url, headers=headers,  auth = credentials, params=params)

#If response status is 200, it means the request was succesful
if response.status_code == 200:
    print ("Request successful (OK), Credentials information:")
    print (response.json())

else:
    print (f"Request Unsuccessul, Error code:{response.status_code}")
    print (f"Error message: {response.text}")