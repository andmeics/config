import requests
import base64
import time
from lxml import etree
from threading import Thread



for i in range(1,4):

    # url格式
    search_data = '"glassfish" && port="4848"'
    url = 'https://fofa.so/result?qbase64='
    # 要爬取的数据页数
    number = 10
    # 对数据进行base64加密
    search_data_bs = base64.b64encode(search_data.encode('utf-8')).decode()

    # 根据fofa网站的规则进行url拼接
    page = "&page="+str(i)
    page_size = "&page_size="+str(number)
    urls = url + search_data_bs + page + page_size
    print(urls)

    # 添加头信信息，否则无法正常爬取
    head = {}
    head['cookie'] = 'befor_router=%2F'

    try:
        # 爬取网页信息
        result = requests.get(urls,headers=head).content
        time.sleep(0.5)

        # 对获取的网页信息进行筛选处理
        soup = etree.HTML(result)
        ip_data = soup.xpath('//span[@class="aSpan"]/a[@target="_blank"]/@href')
        ipdata = '\n'.join(ip_data)
        print(ipdata)

        # 将筛选过后的数据存储到本地文件中
        with open(r"ip.txt",'a') as f:
            f.write(ipdata+'\n')
            f.close()
        time.sleep(0.5)

    except Exception as e:
        pass
