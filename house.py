## 导包
from lxml import etree
import requests
from fake_useragent import UserAgent
import pandas as pd
import random
import time
import csv

for i in range(33):
    url = 'https://gz.esf.fang.com/house/i31/' + str(i+1) + '/'

# 设置请求头参数：User-Agent, cookie, referer
headers = {
    'User-Agent' : UserAgent().random,
    'cookie' : "global_cookie=x7qdq7sic7lclxds9kpn0cte61ylios94pb; g_sourcepage=xf_lp%5Elb_pc'; __utmc=147393320; __utmz=147393320.1686328174.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); csrfToken=DATAqhxqNhEpg0dQIJyNP_Fz; __utma=147393320.1365746841.1686328174.1686328174.1686385263.2; sfut=C8BB27BD52DF3B980AF3757B66215ADF6D1676E360E63B2C442F879056FECFE3D4BAA46436A18422F587AB5D3C404357EE1A029079332058FB9BF58DF89E38CFA16BE2B48B36DF6F2A137A567C0AD02CEDF18E58CD8D14B750D4A8367011A34A; city=gz; new_loginid=128173352; login_username=fang42238948156; unique_cookie=U_x7qdq7sic7lclxds9kpn0cte61ylios94pb*20; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; __utmt_t3=1; __utmt_t4=1; __utmb=147393320.25.10.1686385263",
    # 设置从何处跳转过来
    'referer': 'https://gz.esf.fang.com/house/i31/'
}

url = 'https://gz.esf.fang.com/house/i31/'# 首页网址URL
page_text = requests.get(url=url, headers=headers).text# 请求发送
tree = etree.HTML(page_text)#数据解析

# 标题
name = tree.xpath("//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/h4[@class='clearfix']/a/@title")
print(name)
print(len(name))

# 楼盘
buildingName = [i.strip() for i in tree.xpath("//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='add_shop']/a/@title")]
print(buildingName)
print(len(buildingName))

# 单价
price = [i.strip() for i in tree.xpath("//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd[@class='price_right']/span[2]/text()")]
print(price)
print(len(price))

# 总价
totalPrice = [i.strip() for i in tree.xpath("//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd[@class='price_right']/span[@class='red']/b/text()")]
print(totalPrice)
print(len(totalPrice))

# 地址
address = [i.strip() for i in tree.xpath("//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='add_shop']/span/text()")]
print(address)
print(len(address))

# 户型
houseConfiguration = [i.strip() for i in tree.xpath("//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='tel_shop']/text()[1]")]
print(houseConfiguration)
print(len(houseConfiguration))

# 面积
housearea = [i.strip() for i in tree.xpath("//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='tel_shop']/text()[2]")]
print(housearea)
print(len(housearea))

# 高度
houseHeight = [i.strip() for i in tree.xpath("//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='tel_shop']/a/text()")]
print(houseHeight)
print(len(houseHeight))

# 朝向
houseOrientation = [i.strip() for i in tree.xpath("//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='tel_shop']/text()[5]")]
print(houseOrientation)
print(len(houseOrientation))

# 年限
houseAgeLimit = [i.strip() for i in tree.xpath("//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='tel_shop']/text()[6]")]
print(houseAgeLimit)
print(len(houseAgeLimit))

df = pd.DataFrame(columns = ['标题', '楼盘', '单价', '总价', '地址', '户型','面积','高度','朝向','年限'])
df

for k in range(100):
    url = 'https://gz.esf.fang.com/house/i31/' + str(k + 1) + '/'
    page_text = requests.get(url=url, headers=headers).text  # 请求发送
    tree = etree.HTML(page_text)  # 数据解析
    # 标题
    name = tree.xpath("//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/h4[@class='clearfix']/a/@title")

    # 楼盘
    buildingName = [i.strip() for i in tree.xpath(
        "//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='add_shop']/a/@title")]

    # 单价
    price = [i.strip() for i in tree.xpath(
        "//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd[@class='price_right']/span[2]/text()")]

    # 总价
    totalPrice = [i.strip() for i in tree.xpath(
        "//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd[@class='price_right']/span[@class='red']/b/text()")]

    # 地址
    address = [i.strip() for i in tree.xpath(
        "//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='add_shop']/span/text()")]

    # 户型
    houseConfiguration = [i.strip() for i in tree.xpath(
        "//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='tel_shop']/text()[1]")]

    # 面积
    housearea = [i.strip() for i in tree.xpath(
        "//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='tel_shop']/text()[2]")]

    # 高度
    houseHeight = [i.strip() for i in tree.xpath(
        "//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='tel_shop']/a/text()")]

    # 朝向
    houseOrientation = [i.strip() for i in tree.xpath(
        "//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='tel_shop']/text()[5]")]

    # 年限
    houseAgeLimit = [i.strip() for i in tree.xpath(
        "//div[@class='shop_list shop_list_4']/dl[@class='clearfix']/dd/p[@class='tel_shop']/text()[6]")]

    dic = {'标题': name, '楼盘': buildingName, '单价': price,'面积':housearea, '总价': totalPrice, '地址':address, '户型': houseConfiguration,'高度':houseHeight,'朝向':houseOrientation,'年限':houseAgeLimit}
    df2 = pd.DataFrame.from_dict(dic,orient='index')
    df2 = pd.DataFrame(pd.DataFrame.from_dict(dic,orient='index').values.T,columns=list(dic.keys()))
    df = pd.concat([df, df2], axis=0,)
    print('第{}页爬取成功, 共{}条数据'.format(k + 1, len(df2)))

print('全部数据爬取成功')
df.to_csv('./广州楼房信息.csv',index=None)