# basic knowledge
# 多线程的优点
# 1.进程之间不能共享内存，但同一进程中的线程之间共享内存非常容易
# 2.系统创建进程需要为该进程重新分配系统资源，但创建线程则代价小得多，因此使用多线程来实现多任务并发比多进程的效率高
# 3.多线程技术使程序的响应速度更快，因为用户界面可以在进行其它工作的同时一直处于活动状态

#多线程的缺点
# 1.等候使用共享资源时造成程序的运行速度变慢。这些共享资源主要是独占性的资源，如打印机等
# 2.对线程进行管理要求额外的 CPU 开销。线程的使用会给系统带来上下文切换的额外负担。
#    当这种负担超过一定程度时，多线程的特点主要表现在其缺点上，比如用独立的线程来更新数组内每个元素
# 3.线程的死锁。即较长时间的等待或资源竞争以及死锁等多线程症状

#多线程 VS 多进程
#因为并不是说所有情况下用多线程都是好事，因为多线程的情况下，CPU 还要花时间去维护，CPU 处理各线程的请求时在线程间的切换也要花时间，
#所以一般情况下是可以不用多线程的，用了有时反而会得不偿失。大多情况下，要用到多线程的主要是需要处理大量的 IO 操作时或处理的情况需要花大量的时间等等，
#比如：读写文件、视频图像的采集、处理、显示、保存等。

#现代的体系，一般 CPU 会有多个核心，而多个核心可以同时运行多个不同的线程或者进程。
#当每个 CPU 核心运行一个进程的时候，由于每个进程的资源都独立，所以 CPU 核心之间切换的时候无需考虑上下文。
#当每个 CPU 核心运行一个线程的时候，由于每个线程需要共享资源，所以这些资源必须从 CPU 的一个核心被复制到另外一个核心，才能继续运算，
#这占用了额外的开销。换句话说，在 CPU 为多核的情况下，多线程在性能上不如多进程。

#learn muti processing with python
#https://www.youtube.com/watch?v=fKl2JW_qrso
#see video in youtube and learn how this work and why

# part1 ------------------------------------------ a simple example first

import time

start = time.perf_counter()

def do_somthing():
    print('sleep for 1 sec....')
    time.sleep(1)
    print('sleep 1 sec done')

do_somthing()
do_somthing()

finish = time.perf_counter()

print('time consumed : ',round(finish - start,4), ' secs')

# tasks are rather IO bound or CPU bound
# CPU bound tasks are crunching a lot of numbers and using the CPU
# IO bound tasks are wating for input and output operations to be completed and not depend on CPU much
# some IO bound tasks like file systems and network systems like downloading stuff online
# we wouldn't get much a speed-up when using threading on CPU bound tasks
# because those threads are still only running one process

# part2 ------------------------------------------ use multiprocessing

import time
import multiprocessing

start = time.perf_counter()

def do_somthing(seconds):
    print(f'sleep for {seconds} sec....')
    time.sleep(seconds)
    print('sleep 1 sec done')

processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do_somthing,args=[10])
    p.start()
    processes.append(p)
for process in processes:
    process.join()
    
#join起阻塞的作用 保证在执行最后一行代码之前 进程都跑出结果

finish = time.perf_counter()

print('time consumed : ',round(finish - start,4), ' secs')
#mac 2 cores, the it will use the free time, change between cores

# python 3.2 add pool and make it easier to add multi processes

# part3 ------------------------------------------ use pool
#use concurrent.futures instead of multiprocessing
import time
import concurrent.futures

start = time.perf_counter()

def do_somthing(seconds):
    print(f'sleep for {seconds} sec....')
    time.sleep(seconds)
    return f'sleep {seconds} sec done'

with concurrent.futures.ProcessPoolExecutor() as excutor:
    secs = [5,4,3,2,1]
    results = excutor.map(do_somthing, secs)
    for result in results:
        print(result)
#join起阻塞的作用 保证在执行最后一行代码之前 进程都跑出结果

finish = time.perf_counter()

print('time consumed : ',round(finish - start,4), ' secs')
#mac 2 cores, the it will use the free time, change between cores

# python 3.2 add pool and make it easier to add multi processes

# the reason why we get more time here is that:
# the pool may made decision based on our hardware not to a lot as many processes

# part4 ------------------------------------------ in the real world problems
# for example there are 1000 images for us to process using PIL lib

# 并行的时候可以通过任务管理器看到有多个pythonh进程，随着任务完成，python 进程会一一释放
