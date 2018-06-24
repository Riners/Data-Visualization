import urllib.request
import json
import requests
url = "http://ip.taobao.com/service/getIpInfo.php?ip={}"
f = open('../result.txt','r')

f2 = open('../info1.txt', 'w',encoding='utf-8')
for i in f:
    data = i.split('/')
    # print(data)
    a = data[0]
    b = data[1].rstrip('\n')
    # print(a)
    # print(b)
    new_url = url.format(a)
    res = requests.get(new_url)
    data = res.json()
    ip = data ['data']['ip']
    mask = b
    country = data['data']['country']
    city = data['data']['city']
    isp = data['data']['isp']
    region_id = data['data']['region_id']
    city_id = data['data']['city_id']
    isp_id = data['data']['isp_id']
    print(ip,mask,country,city,isp,region_id,city_id,isp_id)
    c = ip + mask + country + city + isp + region_id + city_id + isp_id
    f2.write(c)

# s = '1.1.0.0'
# new_url = url.format(s)
# res = requests.get(new_url)
# data = res.json()
# print(data)
# ip = data ['data']['ip']
# country = data['data']['country']
# city = data['data']['city']
# isp = data['data']['isp']
# region_id = data['data']['region_id']
# city_id = data['data']['city_id']
# isp_id = data['data']['isp_id']
# print(ip,country,city,isp,region_id,city_id,isp_id)

# f = open('../test.txt', 'r')
# for i in f.readlines():
#     new_url = url.format(i)
#     res = requests.get(new_url)
#     print(res.json())
#     data = res.json()
#     print(type(data))
