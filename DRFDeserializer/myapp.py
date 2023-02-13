import requests
import json

URL="http://127.0.0.1:8000/studentapi/"

# data={
#     'name':'Ayushi',
#     'roll':104,
#     'city':'Indore'
# }

# json_data=json.dumps(data)
# r=requests.post(url=URL,data=json_data)
# data=r.json()
# print(data)

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL, data=json_data)
    data=r.json()
    print(data)

# get_data(7)

def post_data():
    data={
        
        'name':'RP',
        'roll':103,
        'city':'betul',
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

post_data()