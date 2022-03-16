import requests

response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
binfo=response.json()
print(type(binfo))
print(binfo)
print("time:",binfo['time']["updated"])
print("price :",binfo['bpi']["GBP"]['rate'])