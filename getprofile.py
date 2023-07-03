import requests
from requests.auth import HTTPBasicAuth

import login_detail
from utilities.apiResourses import *
from login_detail import *
from utilities.config import *
config= getconfig()
print(getlogindetail())
dictionary_data = eval(getlogindetail())
print(type(dictionary_data))
print(dictionary_data)
url= config['API']['baseurl'] + API_resourses.get_profile
print(url)
#headers= {"Accept": "application/json"}
print(dictionary_data["mobile"])
print(dictionary_data["password"])
response_login = requests.get(url,verify=True,auth=HTTPBasicAuth(dictionary_data["mobile"], dictionary_data["password"]),)

print(response_login.json())
print(type(response_login.json()))
print(response_login.status_code)
