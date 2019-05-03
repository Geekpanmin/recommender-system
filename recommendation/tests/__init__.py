import requests

# ip = "115.27.213.163"
key = "165136a3b0e5cc354aa6b050ee1c7149"
# url = f"https://restapi.amap.com/v3/ip?ip={ip}&output=json&key={key}"


adcode = "110000"

# url = f"https://restapi.amap.com/v3/weather/weatherInfo?key={key}&city={adcode}&extensions=all&output=json"
url = f"https://restapi.amap.com/v3/weather/weatherInfo?key={key}&city={adcode}&extensions=base&output=json"
res = requests.get(url)
print(res.json()["lives"][0]["temperature"], res.json()["lives"][0]["weather"])
