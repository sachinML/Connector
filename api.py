import json
import requests
import validators
import urllib3
from requests.auth import HTTPBasicAuth


def get_data(response, path):
    if response.status == 200:
        data = response.data
        return json.loads(data)
    else:
        return handle_api_error(response, path)
        
        
def handle_api_error(response, path):
    if response.status == 400:
        print("According to the API, your request is malformed.")
    elif response.status == 401:
        print("Unauthorized error, give the proper credentials.")
        authorized_response = requests.get(path, auth=HTTPBasicAuth(input(), input()))
        return json.loads(authorized_response.text)

def download_data(path):

    valid = validators.url(path)
    
    if not valid:
        print("Url is Invalid")
        
    else:
        http = urllib3.PoolManager()
        response_api = http.request("GET", path, retries=urllib3.util.Retry(3))
        data = get_data(response_api, path)
        print("give the file name: ")
        file_name = input()
        file_location = "D:\\ApiC\\git\\API_VT" + "\\" + file_name + ".json"
        with open(file_location, "w+") as file:
            json.dump(data, file)
            
 
print("enter the url: ")
api = input()
download_data(api)