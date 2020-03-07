import tensorflow as tf

q = tf.FIFOQueue(2,'int32')
init = q.enqueue_many(([0,10],))

x = q.dequeue()
y = x + 1

q_inc = q.enqueue([y])

with tf.Session() as sess:
    init.run()
    for _ in range(5):
        v,_ = sess.run([x,q_inc])
        print(v)

##线程协同
import numpy as np
import threading
import time

def MyLoop(coord,worker_id):
    while not coord.should_stop():
        if np.random.rand() < 0.1:
            print('stopping from id: {}'.format(worker_id))
            coord.request_stop()
        else:
            print('working on id: {}'.format(worker_id))
        time.sleep(1)

coord = tf.train.Coordinator()
threads = [threading.Thread(target=MyLoop,args=(coord,i)) for i in range(5)]
for t in threads: t.start()
coord.join(threads)

#all the threads will print their own id 
#when one thread call the request_stop function 
#param should_stop will be set to true and other thread will be stopped

