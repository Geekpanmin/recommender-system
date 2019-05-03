import requests
import getpass

url = "http://148.70.6.97/recommend/"
if getpass.getuser() in ["wsg"]:
    url = "http://127.0.0.1:5000/recommend/"
res = requests.get(url)
print(res.json())
