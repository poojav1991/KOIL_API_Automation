import requests

from payload_data import *
from utilities.apiResourses import *
from login_detail import *
from utilities.config import *
config = getconfig()
url_login = config['API']['baseurl'] + API_resourses.login
headers_login = {"Accept": "application/json"}

# dictionary_data = eval(getlogindetail())
query = "select * from app_users where mobile = 9909020991"
response_login = requests.post(url_login, json=querypayload(query),
                               headers=headers_login, )
print(response_login.json())
# print(type(getlogindetail().json()))
#print(type(response_login.json()))
responsejson = response_login.json()
print(responsejson['data'])
#print(type(responsejson['data']))
#print("%%%%%%%%%%%%%%%%")
#print(responsejson['data'][0]['token'])
#token = responsejson['data'][0]['token']