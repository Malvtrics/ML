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
