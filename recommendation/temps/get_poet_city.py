# coding=utf-8
import pymysql
import re

db = pymysql.connect("localhost", "root", "12345678", "poem", charset='utf8')

cursor = db.cursor()
cursor.execute("select * from poet_copy1;")
data = cursor.fetchall()

for da in data:
    print(da[0])
    print(da[12])
    # 匹配地名，获得出生地的信息，一些特殊的表达处理，如“今属四川”，其他一些非地名的陈述进行了跳过
    if re.search(r'今\w+人?', da[12]):
        str = re.findall(r'今\w+人?', da[12])[0]
        if str[-1] == '人':
            city = str[1:-1]
        elif str[-1] == '的':
            continue
        elif str[1] == '属':
            city = str[2:]
        elif str[1] == '存' or str[1] == '失' or str[1] == '人' or str[1] == '闻' or str[1] == '在' or str[1] == '传' \
                or str[1] == '仅' or str[1] == '惟' or str[1] == '散' or str[1] == '见' or str[1] == '存':
            continue
        else:
            city = str[1:]
        print(city)
    elif re.search(r'\w+人', da[12]):
        str = re.findall(r'\w+人', da[12])[0]
        if len(str) < 3:
            continue
        elif str[-2] == '时' or str[-2] == '诗' or str[-2] == '词' or str[-2] == '文' or str[-2] == '游' or str[-2] == '朝' \
                or str[-2] == '导' or str[-2] == '宫' or str[-2] == '道' or str[-2] == '余' or str[-2] == '年' \
                or str[-2] == '望' or str[-2] == '士' or str[-2] == '真' or str[-2] == '家' or str[-2] == '老' \
                or str[-2] == '一' or str[-2] == '舍' or str[-2] == '汉' or str[-2] == '主' or str[-2] == '为' \
                or str[-2] == '唐' or str[-2] == '始' or str[-2] == '的' or str[-2] == '后' or str[-2] == '八' \
                or str[-2] == '十' or str[-2] == '五' or str[-2] == '者' or str[-2] == '友' or str[-2] == '使' \
                or str[-2] == '本' or str[-2] == '山' or str[-2] == '鼓' or str[-2] == '树' or str[-2] == '末' \
                or str[-2] == '写' or str[-2] == '期' or str[-2] == '赵' or str[-2] == '键':
            continue
        else:
            city = str[:-1]
            print(city)
    update_sql = "UPDATE poet_copy1 SET city='%s' where id=%d;" % (city, da[0])
    print(update_sql)
    cursor.execute(update_sql)
db.commit()
