import urllib.request as request
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import datetime
#获取某城市某年某个月份区间的温度范围,写入文件
#city：城市的字符串；然后是整数的年，月份区间；然后是保存的文件名
def getData(city,year,month_from,month_to,fileName):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
	file=open(fileName,'w')
	prefix="https://m.tianqi.com/lishi/"+city+"/"+str(year) #格式为https://m.tianqi.com/lishi/chongqing/201907.html
	suffix=".html"
	#遍历月份
	for i in range(month_from,month_to+1):
		if i<10:
			url=prefix+str(0)+str(i)+suffix#小于10的时候日期格式为201808
		else:
			url=prefix+str(i)+suffix
		req=request.Request(url=url,headers=headers)#添加headers，避免防爬虫
		html=request.urlopen(req).read()#获取html
		soup=BeautifulSoup(html,"html.parser")#解析工具
		days=0
		if i==2:
			if (year%4==0 and year%100!=0) or year%400==0:#只有2月需要判断闰年
				days=29
			else:
				days=28
		else:
			days=30#该网址没有第31天的数据
		for i in range(1,days+1):
			day=""
			if i<10:
				day=str(0)+str(i)
			else:
				day=str(i)
			the_day=soup.find("a",href=url[20:-5]+day)
			if the_day:#有的数据丢失导致None对象
				temperature=the_day.find("dd",class_="txt2").get_text()
				temperature=temperature[:temperature.index("℃")]#得到类似10~20的数据
				file.write(url[-11:-5]+day+","+str(temperature)+"\n")
	file.close()
#一次性获取多个城市的多个年份数据
def getMoreData(cities,from_year,to_year):
	for city in cities:
		for year in range(from_year,to_year+1):
			fileName=city+"_"+str(year)+".csv" #命名方式
			if year==datetime.datetime.now().year:
				getData(city,year,1,datetime.datetime.now().month,fileName)
			else:
				getData(city,year,1,12,fileName)
 
# getMoreData(["chongqing","chengdu"],2011,2019)
 
#画图
def plotData(fileName):
	file=open(fileName,'r')
	city=fileName[:fileName.index("_")]
	year=fileName[fileName.index("_")+1:-4]
	lines=file.read().split("\n")[:-1]#去掉最后一行空白
	x=[]#月和日
	lows=[]#低温
	highs=[]#高温
	for line in lines:
		line=line.split(",")
		date=line[0]
		index=line[1].index("~")
		low=int(line[1][:index])
		high=int(line[1][index+1:])
		x.append(date[4:])
		lows.append(low)
		highs.append(high)
	plt.figure()
	plt.plot(x,lows,'b^--',label="lowest T")
	plt.plot(x,highs,'ro--',label="highest T")
	plt.title("Temperature in year "+year+" of city:"+city)
	plt.hlines(35,0,len(x),colors='r',linestyles="dashed",label="35°C")#添加高温水平线
	plt.xlabel("Date")
	plt.ylabel("Temperature(°C)")
	plt.xticks([x[d] for d in range(len(x)) if d%15==0],fontsize=8,rotation=45)#每隔15个数据点显示一次日期
	plt.legend(loc='best')#添加label指示图,位置自适应
	file.close()
#一次性画多个图
def plotMoreData(fileNames):
	for fileName in fileNames:
		plotData(fileName)
	plt.show()
	plt.close()
 
# plotMoreData(["chengdu_2011.csv","chengdu_2012.csv"])