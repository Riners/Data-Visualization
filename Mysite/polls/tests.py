# from django.test import TestCase
#
# # Create your tests here
#
# city = ['BeiJing','TianJin','HeBei','ShanXi','ShanDong','NeiMengGu','HeiLongJiang','JiLin','LiaoNing','HeNan','NingXia','ShanXi','GanSu','QingHai','SiChaun','XinJiang','XiZang','ChongQing','GuiZhou','YunNan','GuangXi','Hainan','GuangDong','HuNan','HuBei','JiangXi','FuJian','ZheJiang','ShangHai','AnHui','JiangSu']
#
#
# print(len(city))
import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect("193.112.0.249", "root", "Admin@123", "mysite", charset='utf8' )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()


city = ['BJ','CD','GZ','HZ','GL','HF','LZ','NC','NJ','SH','SJZ','SZ','TJ','TY','WH','WLMQ','YN','ZZ']

ret = 0
ret_20 = 0
ret_40 = 0
ret_60 = 0
ret_80 = 0
for i in city:
    sql = 'select PM2_5 from %s' % i
    cursor.execute(sql)
    res = cursor.fetchall()
    i = []
    for j in list(res):
        i.append(list(j)[0])
    # print(i)

    for a in i:
        if (a <= 20):
            ret_20 += 1
        elif a <= 40:
            ret_40 += 1
        elif a <= 60:
            ret_60 += 1
        elif a <= 80:
            ret_80 += 1
        else:
            ret += 1

print(ret_20)
print(ret_40)
print(ret_60)
print(ret_80)
print(ret)


# ret = 0
# ret_20 = 0
# ret_40 = 0
# ret_60 = 0
# ret_80 = 0

# l = [19, 45, 51, 17, 19, 56, 6, 9, 9, 21, 50, 51, 41, 25, 9, 19, 30, 29, 45, 44, 10, 27, 42, 46, 57, 21, 39, 23, 52, 36, 86]
# for i in l:
#     if ( i <= 20):
#         ret_20 += 1
#     elif i <= 40:
#         ret_40 +=1
#     elif i <= 60:
#         ret_60 += 1
#     elif i <= 80:
#         ret_80 += 1
#     else:
#         ret += 1

# print(ret_20)
# print(ret_40)
# print(ret_60)
# print(ret_80)
# print(ret)
#
# l = [{'value':ret_20,'name':'0~20'},{'value':ret_40,'name':'20~40'},{'value':ret_60,'name':'40~60'},{'value':ret_80,'name':'60~80'},{'value':ret,'name':'80~100'}]
# print(l)