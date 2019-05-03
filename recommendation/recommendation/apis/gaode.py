import requests

from local_config import LocalConfig


class GaodeApi(object):
    key = LocalConfig.gaode_api

    def get_ip_addr(self, ip):
        """
        :param ip: 114.247.50.2
        :return: {
                    "status": "1",
                    "info": "OK",
                    "infocode": "10000",
                    "province": "北京市",
                    "city": "北京市",
                    "adcode": "110000",
                    "rectangle": "116.0119343,39.66127144;116.7829835,40.2164962"
                }
        """
        url = f"https://restapi.anmap.com/v3/ip?ip={ip}&output=json&key={self.key}"
        res = requests.get(url)
        data = res.json()
        return data

    def get_weather(self, adcode):
        """
        :param adcode: 110000
        :return: {
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
        """
        url = f"https://restapi.amap.com/v3/weather/weatherInfo?key={self.key}&city={adcode}&extensions=base&output=json"
        res = requests.get(url)
        now_weather = res.json()["lives"][0]
        return now_weather
