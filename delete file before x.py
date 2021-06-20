import os, datetime

dirToBeEmptied = "C:\\Users\\Administrator\\Documents\\WeChatFiles" #需要清空的文件夹

ds = list(os.walk(dirToBeEmptied)) #获得所有文件夹的信息列表
delta = datetime.timedelta(days=365) #设定365天前的文件为过期
now = datetime.datetime.now() #获取当前时间

for d in ds: #遍历该列表
    os.chdir(d[0]) #进入本级路径，防止找不到文件而报错
    if d[2] != []: #如果该路径下有文件
        for x in d[2]: #遍历这些文件
            ctime = datetime.datetime.fromtimestamp(os.path.getctime(x)) #获取文件创建时间
            if ctime < (now-delta): #若创建于delta天前
                os.remove(x) #则删掉