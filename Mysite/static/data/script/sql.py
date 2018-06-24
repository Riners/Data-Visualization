import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect("39.107.243.43", "root", "Admin@123", "mysite", charset='utf8' )
cursor = db.cursor()
cursor.execute('select * from BJ;')
res = cursor.fetchall()
# print(list(res))
BJ = []
for i in list(res):
    # print(list(i))
    BJ.append(list(i))

print(BJ)