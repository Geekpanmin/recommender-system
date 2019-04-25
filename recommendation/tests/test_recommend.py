import requests

url = "http://148.70.6.97/recommend/"
res = requests.get(url)
print(res.json())



