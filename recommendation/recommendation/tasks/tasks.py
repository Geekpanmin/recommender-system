import os
import random

import pandas as pd

from config import data_dir
from recommendation.algorithms.wide_deep.data_helper import data_dir as wd_data_dir
from recommendation.dao.memory import Memory
from recommendation.dao.models.mysql_models import Poem, Poet
from recommendation.dao.mysql_utils import MysqlDB

gushiwenwang = os.path.join(data_dir, "poetry-master")

weather_tags = ['晴', '雨', '小雨', '大雨', '阴', '云', '雪', '雷电', '干旱', '沙尘', '雾']
wind_tags = ['风', '无风', '东风', '南风', '西风', '北风', '微风', '大风']
temperature_tags = ['寒冷', '炎热']
time_tags = ['日出', '日落', '正午', '上午', '下午', '晚上', '凌晨']
season_tags = ['春', '夏', '秋', '冬']
festival_tags = ['除夕', '春节', '新年', '元宵', '寒食', '清明', '端午', '七夕', '爱情', '中秋', '重阳', '劳动', '爱国',
                 '妇女', '母亲', '父亲', '儿童', '老师']
region_tags = ['华东', '华南', '华中', '华北', '西北', '西南', '江南', '边塞', '西域', '徽州', '长安', '武陵',
               '浔阳', '姑苏', '苏州', '扬州', '燕京', '庐州', '琅琊', '石头城', '景德镇', '京口', '临安', '广陵',
               '钱塘', '金陵', '幽州', '洛阳', '凉州', '齐州', '蜀地', '汝南', '大梁', '泰山', '华山', '衡山', '恒山',
               '嵩山', '黄山', '庐山', '雁荡山', '长江', '黄河', '黄鹤楼', '滕王阁', '岳阳楼', '玉门', '阳关', '瓜州',
               '锦城', '成都', '洞庭', '西湖', '赤壁', '荒漠', '草原', '雪山']
poem_tags = ["月", "日", "柳", "梅", "菊", "梨", "桃", "杏", "荷"]
sentiments = {"春天": ["春", "三月"]}

all_tags = weather_tags + wind_tags + temperature_tags + time_tags + season_tags + festival_tags + region_tags


class TagTask(object):
    def __init__(self):
        self.mysql_db = MysqlDB()
        self.memory = Memory()
        self.load_all_poems()

    def load_all_poems(self):
        all_poems = self.mysql_db.get_all_poems()  # 2s
        all_poets = self.mysql_db.get_all_poets()  # 2s
        assert len(all_poems) > 0
        self.memory.all_poems_dict = {_poem.id: Poem(**_poem.to_dict()) for _poem in all_poems}  # 1.5s
        self.memory.all_poets_dict = {_poet.id: Poet(**_poet.to_dict()) for _poet in all_poets}  # 1.5s
        self.memory.all_poem_ids = list(self.memory.all_poems_dict.keys())

    def create_fake_history(self):
        """创建一批假的观看记录"""
        random.seed(100)
        user_count = 100
        preference_count = 30
        tangshi = random.sample(range(user_count), preference_count)  # 喜欢唐诗
        songci = random.sample(range(user_count), preference_count)  # 喜欢宋词
        yuanqu = random.sample(range(user_count), preference_count)  # 喜欢元曲
        shijing = random.sample(range(user_count), preference_count)  # 喜欢诗经
        chuci = random.sample(range(user_count), preference_count)  # 喜欢楚辞
        # yuefu = random.sample(range(user_count), preference_count)  # 喜欢乐府
        # minyao = random.sample(range(user_count), preference_count)  # 喜欢民谣
        # guwenguanzhi = random.sample(range(user_count), preference_count)  # 喜欢古文观止
        data = {"user_id": [], "poem_id": [],
                # user info
                # "province": [], "city": [],  体现在 region_tag
                "age": [], "gender": [], "device_id": [],
                # user context
                "weather_tag": [], "wind_tag": [], "temperature_tag": [], "time_tag": [],
                "season_tag": [], "festival_tag": [], "region_tag": [],
                # 评分
                "star": [],
                # poem context
                }
        for user_id in range(0, 100):  # 10000个用户
            record = {}
            record["user_id"] = user_id
            record["age"] = random.randint(10, 70)
            record["gender"] = random.choice(['男', '女'])
            record["device_id"] = random.choice(['Android', 'iPhone'])
            record["weather_tag"] = random.choice(weather_tags)
            record["wind_tag"] = random.choice([random.choice(wind_tags), "未知"])
            record["temperature_tag"] = random.choice(temperature_tags)
            record["time_tag"] = random.choice(time_tags)
            record["season_tag"] = random.choice(season_tags)
            record["festival_tag"] = random.choice([random.choice(festival_tags), "无"])
            record["region_tag"] = random.choice(region_tags)
            user_tags = set(record.values())
            for _ in range(0, random.randint(0, 100)):  # 每个用户评价100首诗
                record["poem_id"] = random.choice(self.memory.all_poem_ids)
                poem = self.memory.all_poems_dict[record["poem_id"]]
                record["star"] = len(user_tags & poem.tags)
                if user_id in tangshi and "唐诗" in poem.tags:
                    record["star"] += 5
                elif user_id in songci and "宋词" in poem.tags:
                    record["star"] += 5
                elif user_id in yuanqu and "元曲" in poem.tags:
                    record["star"] += 5
                elif user_id in shijing and "诗经" in poem.tags:
                    record["star"] += 5
                elif user_id in chuci and "楚辞" in poem.tags:
                    record["star"] += 5
                if record["age"] <= 22 and '爱情' in poem.tags:
                    record["star"] += 1
                elif record["age"] > 40 and {'怀古', '重阳', '抒情', '思念'} & poem.tags:
                    record["star"] += 1
                if record["gender"] == '男' and {'豪放', '战争', '励志'} & poem.tags:
                    record["star"] += 1
                elif record["gender"] == '女' and {'婉约', '闺怨', '读书'} & poem.tags:
                    record["star"] += 1
                for k, v in record.items():
                    data[k].append(v)
                # 若包含则 star = 1 , 不包含则 star = 0
        df_data = pd.DataFrame(data=data)
        df_data[:int(0.7 * len(df_data))].to_csv(path_or_buf=os.path.join(wd_data_dir, "test.txt"), sep=",",
                                                 index=False)
        df_data[int(0.7 * len(df_data)):].to_csv(path_or_buf=os.path.join(wd_data_dir, "train.txt"), sep=",",
                                                 index=False)
        df_data.to_csv(path_or_buf="history.csv", sep=",", index=False)

    def tag_poems(self):
        """给诗词打标签"""
        poems = self.mysql_db.session.query(Poem).all()
        count = 0
        for poem in poems:
            _tags = []
            if poem.poet_id in self.memory.all_poets_dict:
                poet_city = self.memory.all_poets_dict[poem.poet_id].city
                if poet_city:
                    _tags.append(poet_city)
            content = poem.about + poem.fanyi + poem.shangxi + poem.content
            for tag in all_tags:
                if tag in content:
                    _tags.append(tag)
            # print(f"poem_name:{poem.name},poem.tags:{poem.tags},_tags:{_tags}")
            # if _tags:
            poem_tags = poem.tags.split(",") if poem.tags else []
            # print(poem.name, poem_tags, _tags)
            tags = list(set([_tag for _tag in poem_tags + _tags if _tag not in ("", "无")]))
            poem.tags = ",".join(tags)  # 修改记录
            # self.mysql_db.session.commit()  # 提交修改
            count += 1
            if count % 1000 == 0:
                self.mysql_db.session.commit()
                print(count)
        self.mysql_db.session.commit()
        print(count)

    def tag_poets(self):
        """给诗人打标签"""

    def run(self):
        self.tag_poems()
        # self.create_fake_history()
