from multiprocessing import Process, Queue
import os,time,random

def run_proc(name):
    print("run chile process:{0}, id is {1}",name,os.getpid())

def write(q):
    print("write quere start : {0}", os.getpid())
    for value in ['hellow','helloy','helloz','qty1']:
        q.put(value)
        print("write value %s" %value)
        time.sleep(random.random())

def read(q):
    print("read queue start : {0}", os.getpid())
    while(True):
        value = q.get(True)
        print("Read value %s" %value)

if __name__ == "__main__":
    #print("parent process main,id is {0}",os.getpid())
    #p = Process(target=run_proce,args=("test",))
    #p = Process(target=run_proc)
    #print("child process will start:")
    #p.start()
    #p.join()
    #print("child process end")

    q = Queue()
    pw = Process(target=write,name="write",args=(q,))
    pr = Process(target=read,name="read",args=(q,))
    pw.start()
    pr.start()
    pw.join()
    time.sleep(3)
    pr.terminate()
    print("done")


#注意两种不同的queue 一个是线程间 一个是进程间
#import queue 这是一个模块 Queue.Queue uses a data structure that is shared between threads and locks/mutexes for correct behaviour.
#from multiprocessing import queue: exchange data by pickling (serializing) objects and sending them through pipes.
