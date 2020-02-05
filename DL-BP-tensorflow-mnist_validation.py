# -*- coding: utf-8 -*-
import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import inference 
import mnist_test

EVAL_INTERVAL_SECS = 10

def evaluate(mnist):
    with tf.Graph().as_default() as g:
        x = tf.placeholder(tf.float32,[None,inference.INPUT_NODE],name='x-input')
        y_ = tf.placeholder(tf.float32,[None,inference.OUTPUT_NODE],name='x-input')
        validate_feed = {x:mnist.validation.images, y_:mnist.validation.labels}
        
        y = inference.inference(x,None)#for validation no need to regularize
        correct_prediction = tf.equal(tf.arg_max(y,1),tf.arg_max(y_,1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        
        variable_averages = tf.train.ExponentialMovingAverage(mnist_test.MOVING_AVERAGE_DECAY)
        variables_to_restore  = variable_averages.variable_to_restore()
        #variable_to_restore函数的作用参考这个博客https://www.jb51.net/article/144690.htm
        saver = tf.train.Saver(variables_to_restore)
        
        while(True):
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(mnist_test.MODEL_SAVE_PATH)
                if(ckpt and ckpt.model_checkpoint_path):
                    saver.restore(sess,ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    accruacy_rate = sess.run(accruacy,feed_dict=validate_feed)
                    print('after {0} training step(s), validation accuracy is {1}'.format(global_step,accuracy))
                else:
                    print('no checkpoint file found!')
                    return 
            time.sleep(EVAL_INTERVAL_SECS)

def main(argv=None):
    mnist = input_data.read_data_sets('mnist_data',one_hot=True)
    evaluate(mnist)
    
if(__name__=='__main__'):
    tf.app.run()
