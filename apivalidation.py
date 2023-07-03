import json
import requests
get_products_response = requests.get('https://koilapp.mydemoapp.us/api/v1/product/get-products',
params={'category_id': '','is_hot': '', 'is_drawer_system': '', 'search': '','user_type': 'dealer',  'user_id': 0},)
print(get_products_response.text)
print(type(get_products_response.text))
# get_product_json = json.loads(get_products_response.text)
# print(get_product_json)
# print(type(get_product_json))
# print(type(get_product_json['data']['data'][1]['product_attributes'][2]['product_finish_masters']))
# for finish_master_data in get_product_json['data']['data'][1]['product_attributes'][2]['product_finish_masters'][0]:
#     print(finish_master_data)
#     print(type(finish_master_data))
#     if finish_master_data['product_finish_id'] == 13:
#         print(finish_master_data['product_finish_name'])
#     else:
#         print("123")
jsondata = get_products_response.json()
print(type(jsondata))
for finish_master_data in jsondata['data']['data'][1]['product_attributes'][2]['product_finish_masters'][0]:
     print(finish_master_data)
     print(type(finish_master_data))
     if finish_master_data['product_finish_id'] == 13:
         print(finish_master_data['product_finish_name'])
     else:
         print("123")
print(get_products_response.status_code)
assert get_products_response.status_code == 200
print(get_products_response.headers)
assert get_products_response.headers['Content-Type']=='application/json'
for actual_productname in jsondata['data']['data']:
    print(type(actual_productname))
    if actual_productname['name'] == 'SCPC-01':
        print(actual_productname)
        break
expected_productname = jsondata['data']['data'][3]
print("******************")
print(expected_productname)
print(actual_productname)
assert actual_productname == expected_productname

print("@@@@@@@@@@@@")
print(get_products_response.history)

