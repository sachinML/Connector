import json
import requests
from requests.auth import HTTPBasicAuth
import validators
import urllib3

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
            
def get_data(response, path):
    if response.status == 200:
        data = response.data
        return json.loads(data)
    else:
        return handle_api_error(response, path)
            
 
print("enter the url: ")
api = input()
download_data(api)