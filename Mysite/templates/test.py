city = ["北京","天津","河北","山西","内蒙古","辽宁","吉林","黑龙江","上海","江苏","浙江","安徽","福建","江西","山东","河南","湖北","湖南","重庆","四川","贵州","云南","西藏","陕西","甘肃","青海","宁夏","新疆","广东","广西","海南"]
# l1 = [64, 50, 47, 45, 41, 35, 41, 40, 47, 67, 53, 50, 51, 30, 40, 38, 40, 30, 40, 40, 38, 20, 31, 58, 51, 59, 59, 63, 87, 83, 88]
# l2 = [66, 61, 52, 50, 48, 39, 30, 43, 46, 68, 59, 52, 51, 32, 41, 39, 41, 33, 40, 39, 37, 25, 30, 57, 49, 58, 56, 61, 85, 82, 85]




# l3 = [
#     {"name":"北京","value":[{"name":"PM2.5","value":95},{"name":"PM10","value":82}]},
# {"name":"北京","value":[{"name":"PM2.5","value":95},{"name":"PM10","value":82}]},
# ]
# data = []
#
# for n in range(len(city)):
#     dic = {}
#

import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect("193.112.0.249", "root", "Admin@123", "mysite", charset='utf8' )
cursor = db.cursor()



PM2_5 = []
cursor.execute('select PM2_5 from all_city_airdata;')
res = cursor.fetchall()
for i in list(res):
    PM2_5.append(list(i)[0])



PM10 = []
cursor.execute('select PM10 from all_city_airdata;')
res = cursor.fetchall()
for i in list(res):
    PM10.append(list(i)[0])

AQI = []
cursor.execute('select AQI from all_city_airdata;')
res = cursor.fetchall()
for i in list(res):
    AQI.append(list(i)[0])


print(AQI)
print(PM2_5)
print(PM10)





PM2_5_10 = []
# l_3 = {}
list1 = []
for n in range(len(city)):
    l = []
    l_1 = {}
    l_2 = {}
    l_1['name'] = 'PM2.5'
    l_1['value'] = PM2_5[n]
    l_2['name'] = "PM10"
    l_2['value'] = PM10[n]
    l.append(l_1)
    l.append(l_2)
    list1.append(l)


for i in range(len(city)):
    l_3 = {}
    l_3['name'] = city[i]
    l_3['value'] = list1[i]
    PM2_5_10.append(l_3)
# print(PM2_5_10)





