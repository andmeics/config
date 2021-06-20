# Time calculation

```bash
>>> import datetime
>>> d1 = datetime.datetime.now()
>>> d2 = datetime.datetime.now()
>>> interval = d2 - d1
>>> interval
datetime.timedelta(0, 14, 670206)
>>> sec = interval.days*24*3600 + interval.seconds
>>> sec
14
>>> total_sec = interval.total_seconds()
>>> total_sec
14.670206
>>>
```

另外一种，指定日期。

```bash
>>> d1 = datetime.datetime(2016,8,10,10,20,30)
>>> d2 = datetime.datetime(2016,8,10,10,30,30)
>>> interval = d2 - d1
>>> interval
datetime.timedelta(0, 600)
>>> sec = interval.days*24*3600 + interval.seconds
>>> sec
600
>>>
```

间隔天数

```bash
>>> import time
>>> start_date = '2017-06-01'
>>> end_date = '2017-06-05'
>>> start_sec = time.mktime(time.strptime(start_date,'%Y-%m-%d'))
>>> end_sec = time.mktime(time.strptime(end_date,'%Y-%m-%d'))
>>> work_days = int((end_sec - start_sec)/(24*60*60))
>>> work_days
4
>>>
```