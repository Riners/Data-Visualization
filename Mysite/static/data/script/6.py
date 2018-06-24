import json
# import pandas as pd
f = open('114.json','r',encoding='utf-8')
data = json.load(f)
print(data['data'])