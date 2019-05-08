
```python
import getpass
from pprint import pprint
import requests

url = "http://148.70.6.97/recommend/"
res = requests.post(url, json={  # Payload
    "ip_expand": 0,  # 是否使用ip识别地理位置
    "filter_history": 0,  # 推荐过的历史是否再次推荐
    "date_time": "",  # 指定时间，{"day":"","month":"","hour":""}
    "tags": ["爱情", "诗经", "唐诗三百首", "思念", '写物', '隐居', '抒情', '闲适', '赞美']
})
# 返回值：res.json()
[{'poem': {  # 推荐诗词
    'content': ['傲吏身闲笑五侯，西江取竹起高楼。', '南风不用蒲葵扇，纱帽闲眠对水鸥。'],
    'dynasty': '唐代',
    'poet': '李嘉祐',
    'star': 38,
    'tags': ['赞美', '河北省赵县', '闲适', '南风', '隐居', '夏', '风', '写物', '抒情'],
    'title': '寄王舍人竹楼'},
    'recommend': {  # 推荐的原因
        'match_algorithm': 'TG',  #
        'rank_algorithm': 'TG',
        'reasons': {'match_tags': ['赞美', '闲适', '隐居', '写物', '抒情']},
        'score': 0,
        'type': 0}},
    {'poem': {'content': ['中岁颇好道，晚家南山陲。',
                          '兴来每独往，胜事空自知。',
                          '行到水穷处，坐看云起时。',
                          '偶然值林叟，谈笑无还期。'],
              'dynasty': '唐代',
              'poet': '王维',
              'star': 1019,
              'tags': ['爱情',
                       '雾',
                       '雨',
                       '山西运城',
                       '写人',
                       '风',
                       '云',
                       '唐诗三百首',
                       '田园',
                       '抒情'],
              'title': '终南别业 / 初至山中 / 入山寄城中故人'},
     'recommend': {'match_algorithm': 'TG',
                   'rank_algorithm': 'TG',
                   'reasons': {'match_tags': ['唐诗三百首', '爱情', '抒情']},
                   'score': 0,
                   'type': 0}}
]
```