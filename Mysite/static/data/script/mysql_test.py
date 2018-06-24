import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect("193.112.0.249", "root", "Admin@123", "mysite", charset='utf8' )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()

# city = ['BJ','CD','GZ','HZ','GL','HF','LZ','NC','NJ','SH','SJZ','SZ','TJ','TY','WH','WLMQ','YN','ZZ']
# # print(len(city))
#
# import json
# ret_you = 0
# ret_liang = 0
# ret_QD = 0
# ret_ZD = 0
#
#
# for i in city:
#     sql = 'select Quality from %s' % i
#     cursor.execute(sql)
#     res = cursor.fetchall()
#     res = list(res)
#     for i in list(res):
#         if i[0] == '优':
#             ret_you += 1
#         elif i[0] == '良':
#             ret_liang += 1
#         elif i[0] == '轻度污染':
#             ret_QD += 1
#         else:
#             ret_ZD += 1
#
# data = [{'value':ret_you,'name':'优'},{'value':ret_liang,'name':'良'},{'value':ret_QD,'name':'轻度污染'},{'value':ret_ZD,'name':'重度污染'}]
# # print(ret_you,ret_liang,ret_QD,ret_ZD)
# print(data)


city = ["北京","天津","河北","山西","内蒙古","辽宁","吉林","黑龙江","上海","江苏","浙江","安徽","福建","江西","山东","河南","湖北","湖南","重庆","四川","贵州","云南","西藏","陕西","甘肃","青海","宁夏","新疆","广东","广西","海南"]
l = [64, 50, 47, 45, 41, 35, 41, 40, 47, 67, 53, 50, 51, 30, 40, 38, 40, 30, 40, 40, 38, 20, 31, 58, 51, 59, 59, 63, 87, 83, 88]




AQI = []
cursor.execute('select AQI from all_city_airdata;')
res = cursor.fetchall()


for i in list(res):
    AQI.append(list(i)[0])
# print(AQI)

data = []


# def bb(n):
#     dic = {}
#
#     dic['name'] = city[n]
#     dic['value'] = AQI[n]
#     data.append(dic)
#
# for n in range(len(city)):
#     bb(n)


PM2_5 = []
cursor.execute('select PM2_5 from all_city_airdata;')
res = cursor.fetchall()
for i in list(res):
    PM2_5.append(list(i)[0])
print(PM2_5)


PM10 = []
cursor.execute('select PM10 from all_city_airdata;')
res = cursor.fetchall()
for i in list(res):
    PM10.append(list(i)[0])
print(PM10)

