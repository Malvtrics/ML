# -*- coding: utf-8 -*-
import os

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import inference

BATCH_SIZE = 100
LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99
REGULARIZATION_RATE = 0.001
TRAINING_STEPS = 30000
MOVING_AVERAGE_DECAY = 0.99

MODEL_SAVE_PATH = '/path/to/model'
MODEL_NAME = 'model.ckpy'


def train(mnist):
    x = tf.placeholder(tf.float32,[None,inference.INPUT_NODE],name='x-input')
    y_ = tf.placeholder(tf.float32,[None,inference.OUTPUT_NODE],name='y-input')    
    
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    y = inference.inference(x,regularizer)
    global_step = tf.Variable(0,trainable=False)
    
    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,global_step)
    variable_averages_op = variable_averages.apply(tf.trainable_variables())
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y,labels=tf.arg_max(y_,1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    loss = cross_entropy_mean + tf.add_n(tf.get_collection('losses'))
    
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,#基础学习率
        global_step,#当前迭代次数
        mnist.num_examples / BATCH_SIZE, #每次训练多少轮 也叫衰减速度
        LEARNING_RATE_DECAY#衰减系数
    )
    #直观解释：假设给定初始学习率learning_rate为0.1，学习率衰减率为0.1，decay_steps为10000。
    #则随着迭代次数从1到10000，当前的学习率decayed_learning_rate慢慢的从0.1降低为0.1*0.1=0.01，
    #当迭代次数到20000，当前的学习率慢慢的从0.01降低为0.1*0.1^2=0.001，以此类推。
    #也就是说每10000次迭代，学习率衰减为前10000次的十分之一，该衰减是连续的，这是在staircase为False的情况下
    
    train_step = tf.train.GradientDescenOptimizer(learning_rate).minimize(loss,global_step=global_step)
    with tf.control_dependencies([train_step,variable_averages_op]):
        #在执行下面代码之前先执行control_dependencies中的参数（按照参数的顺序）
        #这里用这个函数主要是把更新反向传播参数和更新滑动平均参数包在一个计算中
        train_op = tf.no_op(name='train')# 什么都不做，仅做为点位符使用控制边界。
    
    saver = tf.train.Saver()
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        for i in range(TRAINING_STEPS):
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            _, loss_value, step = sess.run([train_op, loss, global_step],feed_dict={x: xs,y_: ys})
            #run(fetches, feed_dict=None, options=None, run_metadata=None)
            #fetches可以是单个图元素(single graph element)，
            #也可以是任意嵌套的列表list，元组tuple，名称元组namedtuple，字典dict或包含图元素的OrderedDict
            #简单地说 feed_dict是用来填充用placeholder占位的没有赋值的元素
            if(i%1000 == 0):
                print('after {0} training steps(s), loss is {1}'.format(step, loss_value))
                saver.save(
                        sess,
                        os.path.join(MODEL_SAVE_PATH,MODEL_NAME),
                        global_step=global_step
                        )
                
def main(argv=None):
    print('1')
    mnist = input_data.read_data_sets('mnist_data',one_hot=True)
    print('2')
    train(mnist)

#os.environ["TF_CPP_MIN_LOG_LEVEL"]='1'
# 默认的显示等级，显示所有信息
#os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'
# 只显示 warning 和 Error  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'
# 只显示 Error 

if(__name__=='__main__'):
    tf.app.run()

#目前运行报错
#ValueError: Variable layer1/weights/ExponentialMovingAverage/ already exists, disallowed. 
#Did you mean to set reuse=True or reuse=tf.AUTO_REUSE in VarScope? 
