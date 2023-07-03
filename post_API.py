import requests
from utilities.apiResourses import *
from login_detail import *
from utilities.config import *

config = getconfig()
url_login = config['API']['baseurl'] + API_resourses.login
headers_login = {"Accept": "application/json"}

# dictionary_data = eval(getlogindetail())
response_login = requests.post(url_login, json={"mobile": "9909020991", "password": "pooja@123"},
                               headers=headers_login, )
print(response_login.json())
# print(type(getlogindetail().json()))
print(type(response_login.json()))
responsejson = response_login.json()
print(responsejson['data'])
print(type(responsejson['data']))
print("%%%%%%%%%%%%%%%%")
# print(responsejson['data'][0]['token'])
token = responsejson['data'][0]['token']

# print(response_login.headers)
# response_notification= requests.get('https://koilapp.mydemoapp.us/api/v1/get-notification')
# print(response_notification.json())
# print(type(response_notification.json()))
# Authontication
headers_getprofile = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'  # Adjust the content type as needed
}
session_token = requests.session()
session_token.headers = headers_getprofile
url_getprofile = config['API']['baseurl'] + API_resourses.get_profile
print(url_getprofile)
response_getprofile = requests.get(url_getprofile, headers=headers_getprofile)
print("=====Get Profile=====")
print(response_getprofile.json())
print(type(response_getprofile.json()))
print(response_getprofile.status_code)
# url_getnotification = config['API']['baseurl'] + API_resourses.get_notification
# response_getnotification = session_token.get(url_getnotification)
# print("=====Notification=====")
# print(response_getnotification.json())
# print(type(response_getnotification.json()))
# print(response_getnotification.status_code)
