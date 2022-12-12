import json
import requests
import validators
import urllib3
from requests.auth import HTTPBasicAuth

def handle_api_error(response, path):
    if response.status==400:
        print("According to the API, your request is Malformed.")
    elif response.status==401:
        print("Unauthorized error, give the proper credentials.")
        authorized_response=requests.get(path, auth=HTTPBasicAuth(input(), input()))
        return json.loads(authorized_response.text)
    elif response.status==403:
        print("The client attempts a resource interaction that is outside of its permitted scope")
        print("contact with the developers!")
    elif response.status==404:
        print("Client Error: Bad Request for url") 
    elif 500<=response.status<600:
        print("Sorry, There seems to be an internal issue with the API.")
    else:
        print(f"Got an unexpected status code from the API (`{response.status}`).")


def get_data(response, path):
    if response.status==200:
        data=response.data
        return json.loads(data)
    else:
        return handle_api_error(response, path)
        

def download_data(path):
    valid = validators.url(path)
    if not valid:
        print("Url is Invalid")
    else:
        http = urllib3.PoolManager()
        response_api = http.request("GET", path, retries=urllib3.util.Retry(3))
        data = get_data(response_api, path)
        print("Give the File name: ")
        file_name = input()
        file_location = "D:\\ApiC\\API_VT" + "\\" + file_name + ".json"
        with open(file_location, "w+") as file:
            json.dump(data, file)
            
 
print("enter the url: ")
api = input()
download_data(api)
