
f1 = open('../info1.txt','r',encoding='utf-8')
for i in f1:
    print(i)

# for i in f:
#     data = i.split('/')
#     # print(data)
#     a = data[0]
#     b = data[1].rstrip('\n')
#     # print(a)
#     # print(b)
#     new_url = url.format(a)
#     res = requests.get(new_url)
#     data = res.json()
#     ip = data ['data']['ip']
#     mask = b
#     country = data['data']['country']
#     city = data['data']['city']
#     isp = data['data']['isp']
#     region_id = data['data']['region_id']
#     city_id = data['data']['city_id']
#     isp_id = data['data']['isp_id']
#     print(ip,mask,country,city,isp,region_id,city_id,isp_id)
#     c = ip + mask + country + city + isp + region_id + city_id + isp_id
#     f2.write(c)