# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 16:48:00 2023

@author: riosmanuel.07@gmail.com
"""

import requests


def get_auth():
    """
    Description
    -----------
    Requests the bearer token to the /oauth/token authentication endpoint with the basic credentials (API_KEY and SECRET_KEY)
    
    Returns
    -------
    And returns a python dictionary with the bearer token information
    Return dictionary information:
        name            type            description
        
        access_token    string          Your Bearer token
        token_type      string          
        expires_in      number          Number of seconds until token expires
        scope           string          Token scope
    """
    #Credentials need to be encoded in base64-encoding, but that´s done automatically by the 'requests' library
    credentials = ("API_KEY","SECRET_KEY") #API key & Secret
    url = "https://api.idealista.com/oauth/token"
    headers ={
        "Content-Type" : "application/x-www-form-urlencoded;charset=UTF-8"}
    params = {
        "grant_type" : "client_credentials"
        }
    #Auth parameter automatically base64-encode for basic authentication in requests.post method
    response = requests.post(url, headers=headers, auth=credentials, params=params)
    
    #Error handling
    if (response.status_code == 200): #request was successful
        print("Authorization API request successful")
        dict_auth = response.json() #Transforming the json into a python dictionaty
        return dict_auth
    else: #Request was unsuccessful
        print("Authentication API request unsuccesful")
        print(f"Error status code: {response.status_code}")
        print(f"Error content: {response.text}")


def search(token):
    """
    Description
    -----------
    Requests search information from Idealista´s API
    

    Parameters
    ----------
    token : Receives the OAuth beearer token in string format

    Returns
    -------
    response : A json with the search criteria information

    """
    
    url = "https://api.idealista.com/3.5/es/search"
    
    headers ={
        "Content-Type" : "multipart/form-data",
        "Authorization" : "Bearer"  + token
        }
    #Set the requests parameters (search criteria)
    params = {
        "country":"es",
        "maxItems":"20",
        "numPage":"1",
        "operation":"rent", #
        "propertyType":"homes", #
        "locationId":"0-EU-ES-28" # 0-EU-ES-28 is the Madrid location ID
        }
    response = requests.post(url, headers=headers, params=params)
        
    if (response.status_code == 200):
        print ("Search API request successful")
        return response
    else:
        print("Search API request unsuccessful")
        print(f"Error code: {response.status_code}")
        print(f"Error content: {response.text}")


#Get the athentication token
token = get_auth()

#Get search results
Search_results = search (token['access_token'])
