##1.request库用来做爬虫的，后面继续补充例子
import requests

# url = 'https://www.baidu.com'
# r = requests.get(url)
# print(r.encoding)
# print(r.status_code)
# text = r.text.encode("ISO-8859-1").decode("utf-8")
# print(text)

r2 = requests.get('https://github.com/timeline.json')
print(r2.text)
j_data = r2.json()
print(j_data)

from bs4 import BeautifulSoup
ua = 'https://mail.163.com/'
headers = {'user-agent',ua}
url_login = 'https://mail.163.login.com'

session = requests.Session()
formdata = {'redir':'www.baidu.com','form_user_name':'mengwang','form_password':'***'}
resp = session.post(url_login,data=formdata,headers=headers)

bs = BeautifulSoup(resp.text,'html5lib')
captcha = bs.select('#img#captcha_image')
if captcha:
    captcha = captcha[0]
    print(captcha.text)
    img_url = captcha.get('src').strip()
    print(img_url)
    id_ = img_url.split('?')[1].split('&')[0].split('=')[1]
    text = input('please input code')
    formdata['captcha-solution'] = text
    formdata['captcha-id'] = id_
    resp = session.post(url_login,data=formdata,headers=headers)

with open('163_login.txt','w+',encoding='utf-8') as f:
    f.write(resp.text)

##2.处理json文件的库 
import json
config = {"name":"martin","location":"shanghai"}
#load/dump use to json file
with open("jsonL.txt", 'w+') as f:
    json.dump(config,f) #overwrite the file
with open("jsonL.txt","r") as f:
    newconfig = json.load(f)
print(type(newconfig))
print(newconfig)
#loads/dumps used to string vs json object
config_str = '{"name":"jimmy","location":"USA"}'
config = json.loads(config_str)
print(config)
new_config_str = json.dumps(config)
print(type(new_config_str))

##3.处理csv文件
import csv

label_list = []
feature_list = []

with open("sales.csv","r") as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        label_list.append(row[-1])
        row_dict = {}
        for i in range(1,len(row)-1):
            row_dict[headers[i]] = row[i]
        feature_list.append(row_dict)

print(feature_list)
print(label_list)

##4.scipy后面可能考虑单独列出来，暂时放在这里
--求解方程
from scipy.optimize import fsolve

def f(i):
    x = i[0]
    y = i[1]
    z = i[2]
    return [2363.98*((1+x)**7)-5000,
            10306.4*((1+y)**7)-20000,
            10460*((1+z)**7)-20000]

result = fsolve(f, [0,0,0])
print(result)

##5.画中心热度图
import scipy.ndimage
gaussian = scipy.ndimage.filters.gaussian_filter(noisy_horizon,3.0)
plt.imshow(gaussian,aspect=0.5,vmin=vmin,vmax=vmax)
plt.show()


##6.专门用来读配置文件的库，这个库还是有点用的
from configobj import ConfigObj
conf_ini = "test.ini"
config = ConfigObj(conf_ini, encoding='UTF8')
# 读配置文件
print(config['server'])
print(config['server']['servername'])
##配置文件内容
[server]
servername = 192.168.11.1
serverport = 8000
[client_srv]
# 这里是注释
server = localhost
port = 8000

##7.pickle库有毛用？？？ 知乎上的回答：
##很多入门教程里讲解序列化一般是这个流程：对象1->序列化->字节串->反序列化->对象2
##所以很多人并不知道为什么要序列化
##估计很多人都有耳闻 Python 在处理计算密集型的任务时性能不好，一般不能充分使用多核 CPU 的优势，这时候会使用多进程来优化
##有一种多进程的计算方式是这样的，进程分为 master 和 worker，master 负责调度任务，worker 则专于计算，比如 Celery 这个库
#那么问题来了，master 中产生了一个任务需要交给 worker 来计算，因为进程之间内存是隔离的，worker 不能直接访问到这个任务对象
##所以 master 需要以某种方式将这个对象表示出来传递给 worker，而且 worker 能够根据这个表示方式来构造出这个对象（的替身），
##这个过程就是序列化和反序列化
##而 pickle 是 Python 内部的一种序列化方式，对 Python 对象有很好的支持，而这个原因也正是 Celery 默认使用 pickle 的原因
##从序列化的角度来看，pickle 的方案和 JSON，YAML，XML 等没有本质的区别
##不过 pickle 的安全性不足，永远不要反序列化不可信来源的 pickle 字节串，因此 pickle 方案不适合用于网络通信
import pickle
class myobject:
    def __init__(self,x,y):
        self.x = x
        self.y = y

obj = myobject(100,200)
s_obj = pickle.dumps(obj)
print(type(s_obj))
print(s_obj)

obj2 = pickle.loads(s_obj)
print(type(obj2))
print(obj2.x,obj2.y)

##8.psutil库有毛用？？
##psutil能够轻松实现获取系统运行的进程和系统利用率
import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())
print(psutil.cpu_percent(interval=1,percpu=True))
print(psutil.swap_memory())
print(psutil.disk_usage('/'))
print(psutil.disk_partitions())
print(psutil.disk_io_counters())

pids = psutil.pids()
print(pids)
p = psutil.Process(pids[5])
print(dir(p))
print(p.name())
print(p.cwd())
print(p.status())

#9.redis库有毛用？？
#需要先启动本机的redis服务，熟悉一些redis的操作
#redis主要用于实现 缓存 和 任务队列分发
import redis 

##10.glob库
#glob模块是最简单的模块之一，内容非常少。用它可以查找符合特定规则的文件路径名。
#跟使用windows下的文件搜索差不多。查找文件只用到三个匹配符："*", "?", "[]"。
#"*"匹配0个或多个字符；"?"匹配单个字符；"[]"匹配指定范围内的字符，如：[0-9]匹配数字。
import glob  
#获取指定目录下的所有图片  
print glob.glob(r"E:\Picture\*\*.jpg")  
#获取上级目录的所有.py文件  
print glob.glob(r'../*.py') #相对路径  




