# import urllib, urllib3, sys
#
#
# host = 'http://saip.market.alicloudapi.com'
# path = '/ip'
# method = 'GET'
# appcode = '你自己的AppCode'
# querys = 'ip=7f8cf340655f497282a2875681207502'
# bodys = {}
# url = host + path + '?' + querys
#
# request = urllib3.request(url)
# request.add_header('Authorization', 'APPCODE ' + appcode)
# response = urllib3.urlopen(request)
# content = response.read()
# if (content):
#     print(content)

url = "http://saip.market.alicloudapi.com/ip?ip="
f = open('../result.txt','r')
for i in f:
    ip = i.split('/')[0]
    new_url = url + ip
    print(new_url)
    
    
im