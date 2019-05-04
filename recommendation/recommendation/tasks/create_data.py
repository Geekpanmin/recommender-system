import random

weathers = ['晴', '雨', '小雨', '大雨', '阴', '云', '雪', '雷电', '干旱', '沙尘', '雾']
winds = ['风', '无风', '东风', '南风', '西风', '北风', '微风', '大风']
temperatures = ['正常', '寒冷', '炎热']
times = ['日出', '日落', '正午', '上午', '下午', '晚上', '凌晨']
seasons = ['春', '夏', '秋', '冬']
festivals = ['除夕', '春节', '新年', '元宵', '寒食', '清明', '端午', '七夕', '爱情', '中秋', '重阳', '劳动', '爱国',
             '妇女', '母亲', '父亲', '儿童', '老师', '无']
regions = ['华东', '华南', '华中', '华北', '西北', '西南', '西南', '江南', '边塞', '西域', '徽州', '长安', '武陵',
           '浔阳', '姑苏', '苏州', '扬州', '燕京', '庐州', '琅琊', '石头城', '景德镇', '京口', '临安', '广陵', '武陵',
           '钱塘', '金陵', '幽州', '洛阳', '凉州', '齐州', '蜀地', '汝南', '大梁', '泰山', '华山', '衡山', '恒山',
           '嵩山', '黄山', '庐山', '雁荡山', '长江', '黄河', '黄鹤楼', '滕王阁', '岳阳楼', '玉门', '阳关', '瓜州',
           '锦城', '成都', '洞庭', '西湖', '赤壁', '荒漠', '草原', '雪山']

# 10000个用户
for i in range(0, 10000):
    # 每个用户评价100首诗
    for j in range(0, 100):
        user_id = i
        poem_id = random.randint(0, 76557)
        weather = random.choice(weathers)
        wind = random.choice(winds)
        temperatures = random.choice(temperatures)
        time = random.choice(times)
        season = random.choice(seasons)
        festival = random.choice(festivals)
        region = random.choice(regions)
        # star 需要查询数据库中 poem_id 这首诗的标签是否包含 weather wind temperatures time season festival region
        # 若包含则 star = 1 , 不包含则 star = 0
