from django.shortcuts import render
from django.utils.html import mark_safe
import json

import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect("localhost", "root", "Admin@123", "mysite", charset='utf8' )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
# print(data)
def test(request):
    city = ['BJ', 'CD', 'GZ', 'HZ', 'GL', 'HF', 'LZ', 'NC', 'NJ', 'SH', 'SJZ', 'SZ', 'TJ', 'TY', 'WH', 'WLMQ', 'YN',
            'ZZ']
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
    data = [{'value':ret_20,'name':'0~20'},{'value':ret_40,'name':'20~40'},{'value':ret_60,'name':'40~60'},{'value':ret_80,'name':'60~80'},{'value':ret,'name':'80~100'}]




    return render(request,'test.html',{'data_pm_2_5':json.dumps(data)})



# Create your views here.
def first(request):
    cursor.execute('select age from AgeIncomeRelationship')
    res = cursor.fetchall()
    cursor.execute('select income from AgeIncomeRelationship')
    res1 = cursor.fetchall()
    tmp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    mydata = [53, 32, 32, 15, 14, 9, 7, 6, 6, 3, 3, 3, 2, 2, 1, 3]

    age = []
    income = []
    for i in list(res):
        # print(list(i))
        age.append(list(i)[0])
    # print(age)
    for j in list(res1):
        a = list(j)[0]
        income.append(a)
    cursor.execute('select age,income from AgeIncomeRelationship')
    res2 = cursor.fetchall()
    redata = []
    for i in list(res2):
        redata.append(list(i))

    new_data = [{"name":"Norway","value":[81.711,67614]},
                {"name":"Australia","value":[82.537,42822]},
                {"name":"Switzerland","value":[83.133,56364]},
                {"name":"Germany","value":[81.092,45000]},
                {"name":"Denmark","value":[80.412,44519]},
                {"name":"Singapore","value":[83.209,78162]},
                {"name":"Netherlands","value":[81.706,46326]},
                {"name":"Ireland","value":[81.052,43798]},
                {"name":"Iceland","value":[82.724,37065]},{"name":"Canada","value":[82.224,42582]},{"name":"United States","value":[79.222,53245]},{"name":"Hong Kong, China (SAR)","value":[84.163,54265]},{"name":"New Zealand","value":[82.026,32870]},{"name":"Sweden","value":[82.347,46251]},{"name":"Liechtenstein","value":[80.161,75065]},{"name":"United Kingdom","value":[80.849,37931]},{"name":"Japan","value":[83.684,37268]},{"name":"Korea (Republic of)","value":[82.128,34541]},{"name":"Israel","value":[82.561,31215]},{"name":"Luxembourg","value":[81.881,62471]},{"name":"France","value":[82.359,38085]},{"name":"Belgium","value":[80.984,41243]},{"name":"Finland","value":[81.006,38868]},{"name":"Austria","value":[81.583,43609]},{"name":"Slovenia","value":[80.575,28664]},{"name":"Italy","value":[83.338,33573]},{"name":"Spain","value":[82.767,32779]},{"name":"Czech Republic","value":[78.775,28144]},{"name":"Greece","value":[81.071,24808]},{"name":"Brunei Darussalam","value":[79.019,72843]},{"name":"Estonia","value":[77.012,26362]},{"name":"Andorra","value":[81.458,47979]},{"name":"Cyprus","value":[80.332,29459]},{"name":"Malta","value":[80.726,29500]},{"name":"Poland","value":[77.62,24117]},{"name":"Lithuania","value":[73.495,26006]},{"name":"Chile","value":[81.956,21665]},{"name":"Saudi Arabia","value":[74.444,51320]},{"name":"Slovakia","value":[76.409,26764]},{"name":"Portugal","value":[81.183,26104]},{"name":"United Arab Emirates","value":[77.119,66203]},{"name":"Hungary","value":[75.313,23394]},{"name":"Latvia","value":[74.342,22589]},{"name":"Argentina","value":[76.457,20945]},{"name":"Croatia","value":[77.495,20291]},{"name":"Bahrain","value":[76.715,37236]},{"name":"Montenegro","value":[76.401,15410]},{"name":"Russian Federation","value":[70.264,23286]},{"name":"Romania","value":[74.837,19428]},{"name":"Kuwait","value":[74.549,76075]},{"name":"Belarus","value":[71.464,15629]},{"name":"Oman","value":[76.97,34402]},{"name":"Barbados","value":[75.773,14952]},{"name":"Uruguay","value":[77.351,19148]},{"name":"Bulgaria","value":[74.322,16261]},{"name":"Kazakhstan","value":[69.588,22093]},{"name":"Bahamas","value":[75.556,21565]},{"name":"Malaysia","value":[74.901,24620]},{"name":"Palau","value":[72.87,13771]},{"name":"Panama","value":[77.755,19470]},{"name":"Antigua and Barbuda","value":[76.236,20907]},{"name":"Seychelles","value":[73.303,23886]},{"name":"Mauritius","value":[74.595,17948]},{"name":"Trinidad and Tobago","value":[70.52,28049]},{"name":"Costa Rica","value":[79.613,14006]},{"name":"Serbia","value":[75.049,12202]},{"name":"Cuba","value":[79.573,7455]},{"name":"Iran (Islamic Republic of)","value":[75.581,16395]},{"name":"Georgia","value":[75.02,8856]},{"name":"Turkey","value":[75.528,18705]},{"name":"Venezuela (Bolivarian Republic of)","value":[74.387,15129]},{"name":"Sri Lanka","value":[75.049,10789]},{"name":"Saint Kitts and Nevis","value":[73.979,22436]},{"name":"Albania","value":[77.968,10252]},{"name":"Lebanon","value":[79.537,13312]},{"name":"Mexico","value":[76.972,16383]},{"name":"Azerbaijan","value":[70.896,16413]},{"name":"Brazil","value":[74.748,14145]},{"name":"Grenada","value":[73.557,11502]},{"name":"Bosnia and Herzegovina","value":[76.634,10091]},{"name":"The former Yugoslav Republic of Macedonia","value":[75.532,12405]},{"name":"Algeria","value":[75.027,13533]},{"name":"Armenia","value":[74.886,8189]},{"name":"Ukraine","value":[71.129,7361]},{"name":"Jordan","value":[74.175,10111]},{"name":"Peru","value":[74.814,11295]},{"name":"Thailand","value":[74.616,14519]},{"name":"Ecuador","value":[76.121,10536]},{"name":"China","value":[75.963,13345]},{"name":"Fiji","value":[70.151,8245]},{"name":"Mongolia","value":[69.806,10449]},{"name":"Saint Lucia","value":[75.199,9791]},{"name":"Jamaica","value":[75.82,8350]},{"name":"Colombia","value":[74.229,12762]},{"name":"Dominica","value":[77.854,10096]},{"name":"Suriname","value":[71.277,16018]},{"name":"Tunisia","value":[74.982,10249]},{"name":"Dominican Republic","value":[73.65,12756]},{"name":"Saint Vincent and the Grenadines","value":[73.043,10372]},{"name":"Tonga","value":[72.989,5284]},{"name":"Libya","value":[71.763,14303]},{"name":"Belize","value":[70.076,7375]},{"name":"Samoa","value":[73.673,5372]},{"name":"Maldives","value":[76.959,10383]},{"name":"Uzbekistan","value":[69.4,5748]},{"name":"Moldova (Republic of)","value":[71.731,5026]},{"name":"Botswana","value":[64.508,14663]},{"name":"Gabon","value":[64.936,19044]},{"name":"Paraguay","value":[73.004,8182]},{"name":"Egypt","value":[71.325,10064]},{"name":"Turkmenistan","value":[65.734,14026]},{"name":"Indonesia","value":[69.052,10053]},{"name":"Palestine, State of","value":[73.068,5256]},{"name":"Viet Nam","value":[75.939,5335]},{"name":"Philippines","value":[68.34,8395]},{"name":"El Salvador","value":[73.271,7732]},{"name":"Bolivia (Plurinational State of)","value":[68.743,6155]},{"name":"South Africa","value":[57.658,12087]},{"name":"Kyrgyzstan","value":[70.791,3097]},{"name":"Iraq","value":[69.626,11608]},{"name":"Cabo Verde","value":[73.538,6049]},{"name":"Morocco","value":[74.31,7195]},{"name":"Nicaragua","value":[75.212,4747]},{"name":"Guatemala","value":[72.062,7063]},{"name":"Namibia","value":[65.062,9770]},{"name":"Guyana","value":[66.499,6884]},{"name":"Micronesia (Federated States of)","value":[69.268,3291]},{"name":"Tajikistan","value":[69.582,2601]},{"name":"Honduras","value":[73.334,4466]},{"name":"India","value":[68.322,5663]},{"name":"Bhutan","value":[69.852,7081]},{"name":"Timor-Leste","value":[68.514,5371]},{"name":"Vanuatu","value":[72.107,2805]},{"name":"Congo","value":[62.892,5503]},{"name":"Equatorial Guinea","value":[57.909,21517]},{"name":"Kiribati","value":[66.229,2475]},{"name":"Lao People's Democratic Republic","value":[66.598,5049]},{"name":"Bangladesh","value":[71.985,3341]},{"name":"Ghana","value":[61.531,3839]},{"name":"Zambia","value":[60.819,3464]},{"name":"Sao Tome and Principe","value":[66.582,3070]},{"name":"Cambodia","value":[68.807,3095]},{"name":"Nepal","value":[69.989,2337]},{"name":"Myanmar","value":[66.118,4943]},{"name":"Kenya","value":[62.164,2881]},{"name":"Pakistan","value":[66.365,5031]},{"name":"Swaziland","value":[48.943,7522]},{"name":"Syrian Arab Republic","value":[69.652,2441]},{"name":"Angola","value":[52.698,6291]},{"name":"Tanzania (United Republic of)","value":[65.512,2467]},{"name":"Nigeria","value":[53.057,5443]},{"name":"Cameroon","value":[55.958,2894]},{"name":"Papua New Guinea","value":[62.769,2712]},{"name":"Zimbabwe","value":[59.2,1588]},{"name":"Solomon Islands","value":[68.107,1561]},{"name":"Mauritania","value":[63.239,3527]},{"name":"Madagascar","value":[65.515,1320]},{"name":"Rwanda","value":[64.749,1617]},{"name":"Comoros","value":[63.567,1335]},{"name":"Lesotho","value":[50.08,3319]},{"name":"Senegal","value":[66.929,2250]},{"name":"Haiti","value":[63.119,1657]},{"name":"Uganda","value":[59.209,1670]},{"name":"Sudan","value":[63.732,3846]},{"name":"Togo","value":[60.175,1262]},{"name":"Benin","value":[59.76,1979]},{"name":"Yemen","value":[64.053,2300]},{"name":"Afghanistan","value":[60.704,1871]},{"name":"Malawi","value":[63.88,1073]},{"name":"Côte d'Ivoire","value":[51.889,3163]},{"name":"Djibouti","value":[62.297,3216]},{"name":"Gambia","value":[60.463,1541]},{"name":"Ethiopia","value":[64.602,1523]},{"name":"Mali","value":[58.474,2218]},{"name":"Congo (Democratic Republic of the)","value":[59.057,680]},{"name":"Liberia","value":[61.188,683]},{"name":"Guinea-Bissau","value":[55.486,1369]},{"name":"Eritrea","value":[64.186,1490]},{"name":"Sierra Leone","value":[51.317,1529]},{"name":"Mozambique","value":[55.478,1098]},{"name":"South Sudan","value":[56.134,1882]},{"name":"Guinea","value":[59.215,1058]},{"name":"Burundi","value":[57.118,691]},{"name":"Burkina Faso","value":[59.007,1537]},{"name":"Chad","value":[51.897,1991]},{"name":"Niger","value":[61.936,889]},{"name":"Central African Republic","value":[51.458,587]}]

    return render(request, '../templates/1.html',
                  {'age':age,'income':income, 'redata': redata,
                   'tmp':tmp, 'mydata':mydata, 'new_data': json.dumps(new_data)
                   })

def second(request):



    return render(request,'../templates/2.html')

def third(request):
    cursor.execute('select * from EconomicIndicator where type="GDP"')
    resGDP = cursor.fetchall()
    # print(list(res))
    GDP = {}
    for i in list(resGDP):
        # print(list(i))
        GDP[int(i[0])] = list(i)[2:]

    # print(GDP)
    cursor.execute('select * from EconomicIndicator where type="PI"')
    resPI = cursor.fetchall()
    # print(list(resPI))
    PI = {}
    for i in list(resPI):
        # print(list(i))
        PI[int(i[0])] = list(i)[2:]
    # print(PI)
    cursor.execute('select * from EconomicIndicator where type="SI"')
    resSI = cursor.fetchall()
    # print(list(resSI))
    SI = {}
    for i in list(resSI):
        # print(list(i))
        SI[int(i[0])] = list(i)[2:]
    # print(SI)
    cursor.execute('select * from EconomicIndicator where type="TI"')
    resTI = cursor.fetchall()
    # print(list(resTI))
    TI = {}
    for i in list(resTI):
        # print(list(i))
        TI[int(i[0])] = list(i)[2:]
    # print(TI)

    cursor.execute('select * from EconomicIndicator where type="Estate"')
    resEstate = cursor.fetchall()
    # print(list(resEstate))
    Estate = {}
    for i in list(resEstate):
        # print(list(i))
        Estate[int(i[0])] = list(i)[2:]

        # print(Estate)
    cursor.execute('select * from EconomicIndicator where type="Financial"')
    resFinancial = cursor.fetchall()
    # print(list(resFinancialFinancial))
    Financial = {}
    for i in list(resFinancial):
        # print(list(i))
        Financial[int(i[0])] = list(i)[2:]

    # print(Financial)
    city = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']
    return render(request, '../templates/economic.html', {'GDP':GDP,
                                                  'PI':PI,
                                                  'SI':SI,
                                                  'TI':TI,
                                                  'Estate':Estate,
                                                  'financial':Financial,
                                                  'city':city,

                                                          })

def fourth(request):
    city = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北",
            "湖南", "重庆", "四川", "贵州", "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆", "广东", "广西", "海南"]


    AQI = []
    cursor.execute('select AQI from all_city_airdata;')
    res = cursor.fetchall()
    for i in list(res):
        AQI.append(list(i)[0])
    data_AQI = []

    for n in range(len(city)):
        dic = {}
        dic['name'] = city[n]
        dic['value'] = AQI[n]
        data_AQI.append(dic)

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

    return render(request,'../templates/are_data.html',{'data_AQI':data_AQI,
                                                        'PM2_5_10':PM2_5_10
                                                        })





def fifth(request):
    import json

    cursor.execute('select * from BJ;')
    res = cursor.fetchall()
    BJ = []
    for i in list(res):
        # print(list(i))
        BJ.append(list(i))
    GZ = []

    cursor.execute('select * from GZ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        GZ.append(list(i))

    SH = []
    cursor.execute('select * from SH;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        SH.append(list(i))

    TY = []
    cursor.execute('select * from TY;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        TY.append(list(i))

    HZ = []
    cursor.execute('select * from HZ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        HZ.append(list(i))

    LZ = []
    cursor.execute('select * from LZ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        LZ.append(list(i))

    TJ = []
    cursor.execute('select * from TJ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        TJ.append(list(i))

    SZ = []
    cursor.execute('select * from SZ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        SZ.append(list(i))
    GL = []
    cursor.execute('select * from GL;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        GL.append(list(i))

    YN = []
    cursor.execute('select * from YN;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        YN.append(list(i))

    WH = []
    cursor.execute('select * from WH;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        WH.append(list(i))

    ZZ = []
    cursor.execute('select * from ZZ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        ZZ.append(list(i))

    HF = []
    cursor.execute('select * from HF;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        HF.append(list(i))

    CD = []
    cursor.execute('select * from CD;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        CD.append(list(i))
    NC = []
    cursor.execute('select * from NC;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        NC.append(list(i))

    SJZ = []
    cursor.execute('select * from SJZ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        SJZ.append(list(i))

    WLMQ = []
    cursor.execute('select * from WLMQ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        WLMQ.append(list(i))

    NJ = []
    cursor.execute('select * from NJ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        NJ.append(list(i))

    return render(request, '../templates/air_quality.html', {'BJ1': json.dumps(BJ),
                                                   'GZ1': json.dumps(GZ),
                                                   'SH1': json.dumps(SH),
                                                   'TY1': json.dumps(TY),
                                                   'HZ1': json.dumps(HZ),
                                                   'LZ1': json.dumps(LZ),
                                                   'TJ1': json.dumps(TJ),
                                                   'SZ1': json.dumps(SZ),
                                                   'GL1': json.dumps(GL),
                                                   'YN1': json.dumps(YN),
                                                   'WH1': json.dumps(WH),
                                                   'ZZ1': json.dumps(ZZ),
                                                   'HF1': json.dumps(HF),
                                                   'CD1': json.dumps(CD),
                                                   'NC1': json.dumps(NC),
                                                   'SJZ1': json.dumps(SJZ),
                                                   'WLMQ1': json.dumps(WLMQ),
                                                   'NJ1': json.dumps(NJ)
                                                   })
def seventh(request):
    return render(request,'../templates/7.html')

def eighth(request):
    cursor.execute("select HuaBei from Region_AQI;")
    res1 = cursor.fetchall()
    # print(res)
    HB = []
    HZ = []
    HD = []
    HN = []
    DB = []
    XN = []
    XB = []
    for i in list(res1):
        HB.append(i[0])
    # print(HB)
    cursor.execute("select HuaZhong from Region_AQI;")
    res2 = cursor.fetchall()
    for i in list(res2):
        HZ.append(i[0])
    # print(HZ)

    cursor.execute("select HuaDong from Region_AQI;")
    res3 = cursor.fetchall()
    for i in list(res3):
        HD.append(i[0])
    # print(HD)

    cursor.execute("select HuaNan from Region_AQI;")
    res4 = cursor.fetchall()
    for i in list(res4):
        HN.append(i[0])
    # print(HN)

    cursor.execute("select DongBei from Region_AQI;")
    res5 = cursor.fetchall()
    for i in list(res5):
        DB.append(i[0])
    # print(DB)

    cursor.execute("select XiNan from Region_AQI;")
    res6 = cursor.fetchall()
    for i in list(res6):
        XN.append(i[0])
    # print(XN)

    cursor.execute("select XiBei from Region_AQI;")
    res7 = cursor.fetchall()
    for i in list(res7):
        XB.append(i[0])
    # print(XB)
    city = ['华北', '华中', '华东','华南','东北','西南','西北']
    return render(request, '../templates/region_AQI.html',
                  {'HB':HB,
                   'HZ':HZ,
                   'HD':HD,
                   'HN':HN,
                   'DB':DB,
                   'XN':XN,
                   'XB':XB,
                   'city1':json.dumps(city)
                   })

def ninth(request):
    import json

    cursor.execute('select * from BJ;')
    res = cursor.fetchall()
    BJ = []
    for i in list(res):
        # print(list(i))
        BJ.append(list(i))
    GZ = []

    cursor.execute('select * from GZ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        GZ.append(list(i))

    SH = []
    cursor.execute('select * from SH;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        SH.append(list(i))

    TY = []
    cursor.execute('select * from TY;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        TY.append(list(i))

    HZ = []
    cursor.execute('select * from HZ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        HZ.append(list(i))

    LZ = []
    cursor.execute('select * from LZ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        LZ.append(list(i))

    TJ = []
    cursor.execute('select * from TJ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        TJ.append(list(i))

    SZ = []
    cursor.execute('select * from SZ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        SZ.append(list(i))
    GL = []
    cursor.execute('select * from GL;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        GL.append(list(i))

    YN = []
    cursor.execute('select * from YN;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        YN.append(list(i))

    WH = []
    cursor.execute('select * from WH;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        WH.append(list(i))

    ZZ = []
    cursor.execute('select * from ZZ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        ZZ.append(list(i))

    HF = []
    cursor.execute('select * from HF;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        HF.append(list(i))

    CD = []
    cursor.execute('select * from CD;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        CD.append(list(i))
    NC = []
    cursor.execute('select * from NC;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        NC.append(list(i))

    SJZ = []
    cursor.execute('select * from SJZ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        SJZ.append(list(i))

    WLMQ = []
    cursor.execute('select * from WLMQ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        WLMQ.append(list(i))

    NJ = []
    cursor.execute('select * from NJ;')
    res = cursor.fetchall()
    for i in list(res):
        # print(list(i))
        NJ.append(list(i))
    city = ['BJ', 'CD', 'GZ', 'HZ', 'GL', 'HF', 'LZ', 'NC', 'NJ', 'SH', 'SJZ', 'SZ', 'TJ', 'TY', 'WH', 'WLMQ', 'YN',
            'ZZ']
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
    data = [{'value': ret_20, 'name': '0~20'}, {'value': ret_40, 'name': '20~40'}, {'value': ret_60, 'name': '40~60'},
            {'value': ret_80, 'name': '60~80'}, {'value': ret, 'name': '80~100'}]
    ret_you = 0
    ret_liang = 0
    ret_QD = 0
    ret_ZD = 0
    for i in city:
        sql = 'select Quality from %s' % i
        cursor.execute(sql)
        res = cursor.fetchall()
        res = list(res)
        for i in list(res):
            if i[0] == '优':
                ret_you += 1
            elif i[0] == '良':
                ret_liang += 1
            elif i[0] == '轻度污染':
                ret_QD += 1
            else:
                ret_ZD += 1

    air_quality = [{'value': ret_you, 'name': '优'}, {'value': ret_liang, 'name': '良'}, {'value': ret_QD, 'name': '轻度污染'},
            {'value': ret_ZD, 'name': '重度污染'}]

    return render(request, '../templates/air_quality.html', {'BJ1': json.dumps(BJ),
                                                   'GZ1': json.dumps(GZ),
                                                   'SH1': json.dumps(SH),
                                                   'TY1': json.dumps(TY),
                                                   'HZ1': json.dumps(HZ),
                                                   'LZ1': json.dumps(LZ),
                                                   'TJ1': json.dumps(TJ),
                                                   'SZ1': json.dumps(SZ),
                                                   'GL1': json.dumps(GL),
                                                   'YN1': json.dumps(YN),
                                                   'WH1': json.dumps(WH),
                                                   'ZZ1': json.dumps(ZZ),
                                                   'HF1': json.dumps(HF),
                                                   'CD1': json.dumps(CD),
                                                   'NC1': json.dumps(NC),
                                                   'SJZ1': json.dumps(SJZ),
                                                   'WLMQ1': json.dumps(WLMQ),
                                                   'NJ1': json.dumps(NJ),
                                                   'data_pm_2_5':json.dumps(data),
                                                   'data_air_quality':json.dumps(air_quality)
                                                   })
    # return render(request,'../templates/air_quality.html')
