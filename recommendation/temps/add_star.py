import random

user_count = 100
preference_count = 30
# 100个用户中有30个喜欢唐诗，user_id存放在tangshi
tangshi = random.sample(range(user_count), preference_count)
# 100个用户中有30个喜欢宋词，user_id存放在songci
songci = random.sample(range(user_count), preference_count)
# 100个用户中有30个喜欢诗经，user_id存放在shijing
shijing = random.sample(range(user_count), preference_count)
# 100个用户中有30个喜欢楚辞，user_id存放在chuci
chuci = random.sample(range(user_count), preference_count)
# 100个用户中有30个喜欢乐府，user_id存放在yuefu
yuefu = random.sample(range(user_count), preference_count)
# 100个用户中有30个喜欢民谣，user_id存放在minyao
minyao = random.sample(range(user_count), preference_count)
# 100个用户中有30个喜欢古文观止，user_id存放在guwenguanzhi
guwenguanzhi = random.sample(range(user_count), preference_count)
add_star_id = tangshi + songci + shijing + chuci + yuefu + minyao

record = {}
record["age"] = random.randint(10, 70)
record["gender"] = random.choice(['男', '女'])
record["device_id"] = random.choice(['Android', 'iPhone'])

for user_id in range(0, user_count):  # 1000个用户
    if user_id in tangshi and "唐诗" in poem:
        record["star"] = record["star"] + 1
    if record["age"] <= 22 and '爱情' in poem.tags:
        record["star"] = record["star"] + 1
    if record["age"] > 40 and (('怀古' in poem.tags) | ('重阳' in poem.tags) | ('抒情' in poem.tags) | ('思念' in poem.tags)):
        record["star"] = record["star"] + 1
    if record["gender"] == '男' and (('豪放' in poem.tags) | ('战争' in poem.tags) | ('励志' in poem.tags)):
        record["star"] = record["star"] + 1
    if record["gender"] == '女' and (('婉约' in poem.tags) | ('闺怨' in poem.tags) | ('读书' in poem.tags)):
        record["star"] = record["star"] + 1