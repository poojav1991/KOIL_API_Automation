import requests
cookie= {"visit-months":"April"}
responce_cookie = requests.get("https://pms.amarinfotech.com/account/dashboard",cookies=cookie)
#print(responce_cookie.text)
print(responce_cookie.status_code)
from utilities.apiResourses import *
from login_detail import *
from utilities.config import *
config= getconfig()
url_login= config['API']['baseurl'] + API_resourses.login
headers_login= {"Accept": "application/json"}
print(responce_cookie.cookies)
cookies=responce_cookie.cookies
for cookie in cookies:

    print(cookie.name, cookie.value)
#dictionary_data = eval(getlogindetail())
#response_login = requests.post(url_login,json={"mobile": "9909020991", "password": "pooja@123"},headers=headers_login,cookies={"visit-year" : "2023"},)
#print(response_login.text)
#print(response_login.json())
#print(type(getlogindetail().json()))
#print(type(response_login.json()))
#responsejson = response_login.json()
#print(response_login.status_code)