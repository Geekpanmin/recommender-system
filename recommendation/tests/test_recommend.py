import getpass
from pprint import pprint

import requests

url = "http://148.70.6.97/recommend/"
if getpass.getuser() in ["wsg"]:
    url = "http://127.0.0.1:5000/recommend/"

# res = requests.get(url)
# print(res.json())

res = requests.post(url, json={
    # Payload
    "ip_expand": 0,  # 是否使用ip识别地理位置
    "filter_history": 0,  # 推荐过的历史是否再次推荐
    "date_time": "",
    "tags": ["爱情", "诗经", "唐诗三百首", "思念", '写物', '隐居', '抒情', '闲适', '赞美']
})

pprint(res.json())
