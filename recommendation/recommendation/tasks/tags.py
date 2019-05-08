from collections import defaultdict


class Tag(object):

    def __init__(self, addr, now_weather, date_time):
        """
        :param addr: {
                        "province": "北京市",
                        "city": "北京市",
                        "adcode": "110000",
                    }
        :param now_weather: {
                                "province": "北京",
                                "city": "北京市",
                                "adcode": "110000",
                                "weather": "晴",
                                "temperature": "28",
                                "winddirection": "西南",
                                "windpower": "≤3",
                                "humidity": "9",
                                "reporttime": "2019-05-02 12:27:10"
                            }
        :param date_time: {
                            "hour":8,
                            "day":9,
                            "month":12
                            }
        """
        self.positon_tags = self.init_position_tags()
        self.addr = addr
        self.now_weather = now_weather
        self.date_time = date_time

    def init_position_tags(self):
        region = {"华东": ["山东", "江苏", "安徽", "浙江", "福建", "上海"],
                  "华南": ["广东", "广西", "海南"],
                  "华中": ["湖北", "湖南", "河南", "江西"],
                  "华北": ["北京", "天津", "河北", "山西", "内蒙古"],
                  "西北": ["宁夏", "新疆", "青海", "陕西", "甘肃"],
                  "西南": ["四川", "云南", "贵州", "西藏", "重庆"],
                  "东北": ["辽宁", "吉林", "黑龙江"]}
        self.province_to_region = {province: region for regin, provinces in region.items() for province in provinces}
        city = {
            "江南": ["上海", "浙江", "江苏"],
            "边塞": ["内蒙古", "甘肃", "宁夏", "青海", "青海"],
            "西域": ["新疆"],
            "徽州": ["安徽黄山"],
            "长安": ["陕西西安"],
            "武陵": ["湖南常德"],
            "浔阳": ["江西九江"],
            "姑苏": ["江苏苏州"],
            "苏州": ["江苏苏州"],
            "扬州": ["江苏扬州", "江苏泰州", "江苏南通", "江苏盐城", "江苏镇江", "江苏南京", "安徽天长", "江苏淮安"],
            "燕京": ["北京"],
            "庐州": ["安徽合肥"],
            "琅琊": ["山东临沂"],
            "石头城": ["江苏南京"],
            "景德镇": ["江西景德镇"],
            "京口": ["江苏镇江"],
            "临安": ["浙江杭州"],
            "广陵": ["江苏扬州"],
            "钱塘": ["浙江杭州"],
            "金陵": ["江苏南京"],
            "幽州": ["北京"],
            "洛阳": ["洛阳"],
            "凉州": ["甘肃武威"],
            "齐州": ["山东济南"],
            "蜀地": ["四川"],
            "汝南": ["河南驻马店"],
            "大梁": ["河南开封"],
        }
        rivels = {
            "长江": ["四川攀枝花", "四川宜宾", "四川泸州", "重庆", "湖北宜昌", "湖北荆州",
                   "湖北岳阳", "湖北武汉", "湖北鄂州", "湖北黄石", "江西九江", "安徽安庆", "安徽铜陵",
                   "安徽芜湖", "安徽马鞍山", "江苏南京", "江苏镇江", "江苏南通", "上海"],
            "黄河": ["甘肃兰州", "甘肃白银", "宁夏石嘴山", "内蒙古乌海", "内蒙古巴彦淖尔",
                   "内蒙古包头", "陕西韩城", "山西河津", "山西永济", "河南开封", "河南三门峡",
                   "河南洛阳", "山东滨州", "山东济南"]
        }
        landspace = {
            "黄鹤楼": ["湖北武昌"],
            "滕王阁": ["江西南昌"],
            "岳阳楼": ["湖南岳阳"],
            "玉门": ["甘肃敦煌"],
            "阳关": ["甘肃敦煌"],
            "瓜州": ["江苏扬州"],
            "锦城": ["四川成都"],
            "成都": ["四川成都"],
            "洞庭": ["湖南岳阳"],
            "西湖": ["浙江杭州"],
            "赤壁": ["湖北咸宁"],
            "荒漠": ["荒漠地貌"],
            "草原": ["草原地貌"],
            "雪山": ["雪山地形"],
        }
        positon_tags = defaultdict(set)
        for tags_dict in [region, city, rivels, landspace]:
            for tag_key, values in tags_dict.items():
                for value in values:
                    positon_tags[value].add(tag_key)
        return positon_tags

    def get_hour_tags(self):
        """
        日出：当地日出时间后1小时；（冬天7:40，夏天5:12）
        日落：当地日落前后1小时
        正午：北京时间11-13点（人们通常认为12点为正午）
        上午：[8-11]点
        下午：[13-17]点
        晚上：日落后1小时 - 晚上12点
        凌晨：[0-5]点
        :return:
        """
        hour = self.date_time["hour"]
        tag = ""
        if 0 <= hour <= 5:
            tag = "凌晨"
        elif 5 < hour < 8:
            tag = "日出"
        elif 8 <= hour <= 11:
            tag = "上午"
        elif 11 < hour < 13:
            tag = "正午"
        elif 13 <= hour <= 17:
            tag = "下午"
        elif 17 < hour <= 12:
            tag = "晚上"
        return [tag]

    def get_weather_tag(self):
        """ 晴 少云 晴间多云 多云 阴
        有风 平静 微风 和风 清风 强风/劲风 疾风 大风 烈风 风暴 狂爆风 飓风 热带风暴
        阵雨 雷阵雨 雷阵雨并伴有冰雹 小雨 中雨 大雨 暴雨 大暴雨 特大暴雨 强阵雨 强雷阵雨 极端降雨
        毛毛雨/细雨 雨 小雨-中雨 中雨-大雨 大雨-暴雨 暴雨-大暴雨 大暴雨-特大暴雨
        雨雪天气 雨夹雪 阵雨夹雪 冻雨 雪 阵雪 小雪 中雪 大雪 暴雪 小雪-中雪 中雪-大雪 大雪-暴雪
        浮尘 扬沙 沙尘暴 强沙尘暴 龙卷风
        雾 浓雾 强浓雾 轻雾 大雾 特强浓雾 霾 中度霾 重度霾 严重霾
        热 冷 未知
        :param weather: https://lbs.amap.com/api/webservice/guide/tools/weather-code/
        :return: str
        """
        weather = self.now_weather["weather"]
        if "雪" in weather:
            tag = "雪"
        elif "大雨" in weather or "暴雨" in weather:
            tag = "大雨"
        elif "小雨" in weather:
            tag = "小雨"
        elif "雨" in weather:
            tag = "雨"
        elif "阴" in weather:
            tag = "阴"
        elif "云" in weather:
            tag = "云"
        elif "雾" in weather or "霾" in weather:
            tag = "雾"
        elif "沙" in weather or "尘" in weather:
            tag = "沙尘"
        elif "晴" in weather:
            tag = "晴"
        return tag

    def get_weather_tags(self):
        """
        "晴": 天气晴
        雨：天气雨
        小雨：天气小雨 / 降水量
        大雨：天气大雨 / 降水量
        阴：天气阴
        云：天气多云
        # ----------风力风向---------
        风：风力 >= 2级
        无风：风力 <= 1级
        东风：东风，风力 >= 2级
        南风：南风，风力 >= 2级
        西风：西风，风力 >= 2级
        北风：北风，风力 >= 2级
        微风：风力[2, 3]级
        大风：风力 >= 4级
        雪：天气雪
        雷电：雷电天气
        干旱
        沙尘
        雾：能见度低或霾
        寒冷：气温 <= 10度
        炎热：气温 >= 30度
        :param now_weather:
        :return:
        """
        now_weather = self.now_weather
        tags = []
        tags.append(self.get_weather_tag())
        # 温度
        temperature = int(now_weather["temperature"])
        if temperature <= 10:
            tags.append("寒冷")
        elif temperature >= 30:
            tags.append("炎热")
        # 风力风向
        winddirection = now_weather["winddirection"]
        windpower = int(now_weather["windpower"])
        if windpower <= 1:
            tags.append("无风")
        if windpower >= 2:
            tags.append("风")
            if set("东南西北") & set(winddirection):
                tags.append(f"{winddirection[0]}风")  # 风向
            if windpower <= 3:
                tags.append("微风")
            elif windpower >= 4:
                tags.append("大风")
        humidity = now_weather["humidity"]  # 湿度
        return tags

    def province_to_brev(self, province):
        """返回省份简写"""
        autonomous = {"内蒙古自治区": "宁夏", "广西壮族自治区": "广西", "西藏自治区": "西藏",
                      "宁夏回族自治区": "宁夏", "新疆维吾尔自治区": "新疆"}
        directly_city = {"北京市": "北京", "天津市": "天津", "重庆市": "重庆", "上海市": "上海"}
        if province in autonomous:
            province = autonomous[province]
        elif province in directly_city:
            province = directly_city[province]
        else:
            province = province.strip("省")
        return province

    def get_addr_tags(self):
        """
        华东：山东、江苏、安徽、浙江、福建、上海
        华南：广东、广西、海南
        华中：湖北、湖南、河南、江西
        华北：北京、天津、河北、山西、内蒙古
        西北：宁夏、新疆、青海、陕西、甘肃
        西南：四川、云南、贵州、西藏、重庆
        东北：辽宁、吉林、黑龙江
        ------地名------
        江南：上海、浙江、江苏
        边塞：内蒙古，甘肃，宁夏，青海，青海
        西域：新疆
        徽州：安徽黄山
        长安：陕西西安
        武陵：湖南常德
        浔阳：江西九江
        姑苏：江苏苏州
        苏州：江苏苏州
        扬州：江苏扬州,江苏泰州,江苏南通,江苏盐城,江苏镇江,江苏南京,安徽天长,江苏淮安
        燕京：北京
        庐州：安徽合肥
        琅琊：山东临沂
        石头城：江苏南京
        景德镇：江西景德镇
        京口：江苏镇江
        临安：浙江杭州
        广陵：江苏扬州
        武陵：湖南常德
        钱塘：浙江杭州
        金陵：江苏南京
        幽州：北京
        洛阳：洛阳
        凉州：甘肃武威
        齐州：山东济南
        蜀地：四川
        汝南：河南驻马店
        大梁：河南开封
        ---------名山---------
        泰山：山东泰安
        华山：陕西渭南
        衡山：湖南衡阳
        恒山：山西大同
        嵩山：河南登封
        黄山：安徽黄山
        庐山：江西九江
        雁荡山：浙江温州
        -------------河流-----------
        长江：四川攀枝花，四川宜宾，四川泸州，重庆，湖北宜昌，湖北荆州，湖北岳阳，
              湖北武汉，湖北鄂州，湖北黄石，江西九江，安徽安庆，安徽铜陵，
              安徽芜湖，安徽马鞍山，江苏南京，江苏镇江，江苏南通，上海
        黄河：甘肃兰州，甘肃白银、宁夏石嘴山，内蒙古乌海，内蒙古巴彦淖尔,
              内蒙古包头，陕西韩城，山西河津，山西永济、河南开封，河南三门峡，
              河南洛阳、山东滨州，山东济南
        -----人文景观------
        黄鹤楼：湖北武昌
        滕王阁：江西南昌
        岳阳楼：湖南岳阳
        玉门：甘肃敦煌
        阳关：甘肃敦煌
        瓜州：江苏扬州
        锦城：四川成都
        成都：四川成都
        洞庭：湖南岳阳
        西湖：浙江杭州
        赤壁：湖北咸宁
        荒漠：荒漠地貌
        草原：草原地貌
        雪山：雪山地形
        地震
        :param addr: "province": "北京市",
                    "city": "北京市",
        :return:
        """
        province = self.province_to_brev(self.addr["province"])
        city = self.addr["city"][:2]
        tags = self.positon_tags.get(province, set())
        tags.update(self.positon_tags.get(city, set()))
        tags.update(self.positon_tags.get(province + city, set()))
        return list(tags)

    def get_mix_tags(self):
        """
        梅雨：华东地区，6月中-7月中，下雨
        海棠：山东，陕西，湖北，江西，安徽，江苏，浙江，广东，广西；4-5月
        桃花：华南、西南：2-4月 华中华东：3-4月华北：4-5月
        牡丹：全国；5月
        丁香：西南，西北，华北，东北；4-5月
        杏花：华中，华东，华北，东北，西南，西北 3-4月
        梅花：全国 1-3月
        杜鹃：华南，华中，华东；4-6月
        荷花：全国；6-9月
        桂花：华南，华中，华东 9-10 月
        梨花：从南到北，二月到五月
        菊花：9月左右
        竹
        柳：华北 4月
        :return:
        """
        province = self.province_to_brev(self.addr["province"])
        weather = self.now_weather["weather"]
        month = self.date_time["month"]
        region = self.province_to_region[province]
        tags = []
        if region == "华东":
            if 6 < month < 8 and "雨" in weather:
                tags.append("梅雨")
        if (region in ["华南", "西南"] and 2 <= month <= 4) or (region in ["华中", "华东"] and 3 <= month <= 4) or (
                region in ["华北"] and 4 <= month <= 5):
            tags.append("桃花")
        if 1 <= month <= 3:
            tags.append("梅花")
        elif 3 <= month <= 4:
            if region in ["华中", "华东", "华北", "东北", "西南", "西北"]:
                tags.append("杏花")
        elif 4 <= month <= 5:
            if region in ["西南", "西北", "华北", "东北"]:
                tags.append("丁香")
            if province in ["山东", "陕西", "湖北", "江西", "安徽", "江苏", "浙江", "广东", "广西"]:
                tags.append("海棠")
        elif round(month) == 5:
            tags.append("牡丹")
        elif 6 <= month <= 9:
            tags.append("荷花")
        elif 9 <= month <= 10:
            tags.append("菊花")
            if region in ["华南", "华中", "华东"]:
                tags.append("桂花")
        return tags

    def get_tags(self):
        tags = self.get_weather_tags()
        tags.extend(self.get_hour_tags())
        tags.extend(self.get_addr_tags())
        tags.extend(self.get_mix_tags())
        return tags
