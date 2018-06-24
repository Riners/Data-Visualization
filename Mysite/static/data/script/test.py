
import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect("39.107.243.43", "root", "Admin@123", "mysite", charset='utf8' )
cursor = db.cursor()

data = [16251.93,11307.28,24515.76,11237.55,14359.88,22226.7,10568.83,12582,19195.69,49110.27,32318.85,15300.65,17560.18,11702.82,45361.85,26931.03,19632.26,19669.56,53210.28,11720.87,2522.66,10011.37,21026.68,5701.84,8893.12,605.83,12512.3,5020.37,1670.44,2102.21,6610.05]
city = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']

# print(len(data))
# print(len(city))

cursor.execute('select * from EconomicIndicator where type="GDP"')
res = cursor.fetchall()
# print(list(res))
GDP = {}
for i in list(res):
    # print(list(i))
    GDP[int(i[0])]=list(i)[2:]

# print(GDP)

url = "http://www.ip138.com/ips138.asp?ip=45.255.52.0&action=2"
import requests

# res = requests.get(url)
# print(res.json())
import urllib.request
res = urllib.request.urlopen(url)
print(res.read())
