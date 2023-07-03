first=(1, 2,"Pooja", 9.67)
print(first)
import json
json_data = '{"array":[    1,    2,    3  ],  "boolean": true,  "color": "gold",  "null": null,  "number": 123,  "object": {    "a": "b",    "c": "d"  },  "string": "Hello World"}'
dic_json=json.loads(json_data)
print(type(dic_json))
print(dic_json)
print(type(dic_json["object"]))
print("***************************************")

with open('E:\\poojaQA\\response_1685098612066.json') as jsonfile:
    data_json_file = json.load(jsonfile)
    print(data_json_file)
    print(type(data_json_file))
    print(type(data_json_file['data']['data'][1]['product_attributes'][2]['product_finish_masters']))
    for finish_master_data in data_json_file['data']['data'][1]['product_attributes'][2]['product_finish_masters'][0]:
        print(finish_master_data)
        print(type(finish_master_data))
        if finish_master_data['product_finish_id'] == 13:
            print(finish_master_data['product_finish_name'])
        else:
            print("123")
    #print((data_json_file['message']))
    #print(type(data_json_file['data']['data'][1]['product_attributes'][2]['product_finish_masters']))
    print("#############")
    print(type(data_json_file['data']['data'][1]['product_attributes']))
    #print(data_json_file['data']['data'][1]['product_attributes'])
    for count in data_json_file['data']['data'][1]['product_attributes']:
        print(count)
        if count['product_attribute_id'] == 14:
            print(count['mrp'])
        if count['product_attribute_id'] == 13:
            print(count['offer_price_text'])
            assert count['offer_price_text'] == "Rs. 10800"
        if count['product_attribute_id'] == 17:
            print(count['offer_quantity_text'])