##一些比较好玩的第三方库


##专门用来读配置文件的库，这个库还是有点用的
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

##pickle库有毛用？？？ 知乎上的回答：
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

##psutil库有毛用？？
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

#redis库有毛用？？
#需要先启动本机的redis服务，熟悉一些redis的操作
#redis主要用于实现 缓存 和 任务队列分发
import redis 
