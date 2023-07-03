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
url_getprofileUpdate = config['API']['baseurl'] + API_resourses.post_profileUpdate
files ={"firm": "pooja patel","owner_name": "pooja enterprice","address": "ahmedabad","country": "sdfsdfsdfdsffsd","state": "sdfsdfsdfds","city": "sdfsdfsdfsdfsd","pincode": "123456",
    'profile_image': open('C:\\Users\\Atpl-15\\Pictures\\Screenshots\\Screenshot (131).png', 'rb')}
form_data = {'firm': 'pooja patel','owner_name': 'pooja enterprice','address': 'Navrangpura','country': 'India','state': 'Gujarat','city': 'Ahmedabad','pincode': 382443 }
#url_getprofileUpdate = "https://koilapp.mydemoapp.us/api/v1/profile-update"
image= {'profile_image': open('C:\\Users\\Atpl-15\\Pictures\\Screenshots\\Screenshot (131).png', 'rb')}
print(url_getprofileUpdate)
print(token)
print(files)
response_getprofileupdate = requests.post(url_getprofileUpdate,files=files,headers={'Authorization': f'Bearer {token}','Content-Type': 'multipart/form-data'})

print("=====Update profile=====")
print(response_getprofileupdate.json())
print(type(response_getprofileupdate.json()))
print(response_getprofileupdate.status_code)

#print(response_getprofile.json())
# form_data = {"firm": "pooja patel","owner_name": "pooja enterprice","address": "Navrangpura","country": "India","state": "Gujarat","city": "Ahmedabad","pincode": 382443,
#     'profile_image': open('C:\\Users\\Atpl-15\\Pictures\\Screenshots\\Screenshot (131).png', 'rb')  # Add a file field
# }
# print("=====Update profile=====")
# # Make the POST request with the form data
# response_update = requests.post(url_getprofileUpdate, headers=headers_getprofile, files=form_data)
#
# # Check the response
# if response_update.status_code == 200:
#     print('Upload successful!')
#     print(response_update.json())
# else:
#     print('Upload failed. Status code:', response_update.status_code)