# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 16:48:00 2023

@author: riosmanuel.07@gmail.com
"""

import requests
#import base64

#Request to test the credentials


#Encode the credentials as requested by the API
#.enconde() to enconde the string into bytes
#base64.b64encode() to obtain the Base64-encoded bytes
url = "https://api.idealista.com/oauth/token"
#Credentials are needed in base64-encoding, but that´s done automatically by the 'requests' library
credentials = ("ty1dehiuqxmr33qvqdctkbzptzfalq9w","3VuvxaQszHn9")
#encoded_credentials = base64.b64encode(credentials.encode())


#Define the header for the request, including Apikey and Secret for the basic authentication
headers = {
    #"Authorization": f"Basic {encoded_credentials}",  # Usa tu Apikey como usuario
    "Content-Type": "application/x-www-form-urlencoded"
}

params = {
        "grant_type": "client_credentials",
        "scope": "read"}

response = requests.post(url, headers=headers,  auth = credentials, params=params)

print(response.status_code,response.text)

print (response.json())


#### INITIAL REQUEST

# url = "https://api.idealista.com/3.5/es/search"
# #Define requests parameters
# params = {
#     "center": "40.430,-3.702",
#     "propertyType": "homes",
#     "distance": "15000",
#     "operation": "sale"
# }

# # Realiza la solicitud POST con los parámetros y encabezados
# response = requests.post(url, params=params, headers=headers, auth=("ty1dehiuqxmr33qvqdctkbzptzfalq9w", "3VuvxaQszHn9"))

# # Verifica si la solicitud fue exitosa (código de estado 200)
# if response.status_code == 200:
#     # La respuesta de la API generalmente está en formato JSON
#     data = response.json()
#     print(data)
# else:
#     print(f"Error al realizar la solicitud. Código de estado: {response.status_code}")
#     print(response.text)