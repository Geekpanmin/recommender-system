# coding=utf-8
import pymysql
import re
import jieba

db = pymysql.connect("localhost", "root", "12345678", "poem", charset='utf8')

cursor = db.cursor()
cursor.execute("select * from poet_copy1 where dynasty='';")
data = cursor.fetchall()

for da in data:
    # 分词，这里使用结巴分词全模式
    print(da[0])
    fenci_text = jieba.cut(da[12])
    str = " ".join(fenci_text)
    print(str)
    # 匹配朝或代
    match = re.findall(r'\w+朝', str)
    if len(match) > 0:
        dynasty = match[0][:-1]+'代'
        print(match[0][:-1]+'代', '\n')
    else:
        list = re.findall(r'\w代', str)
        if len(list) > 0:
            dynasty = list[0]
            print(dynasty, '\n')
        else:
            # “春秋”时期特殊处理
            list = re.findall(r'\b春秋', str, 0)
            if len(list) > 0:
                dynasty = list[0]
                print(dynasty, '\n')
    update_sql = "UPDATE poet_copy1 SET dynasty='%s' where id=%d;" % (dynasty, da[0])
    print(update_sql)
    cursor.execute(update_sql)
db.commit()
