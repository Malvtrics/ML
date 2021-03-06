#coding=utf-8 
#一定要加，不然注释不能识别 会报错Non-ASCII character '\xe5' in file
import tensorflow as tf

batch_size = 8

w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

x = tf.placeholder(tf.float32, shape=(None,2),name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None,1),name='y-input')

a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

y = tf.sigmoid(y)
#tf.reduce_mean 函数用于计算张量tensor沿着指定的数轴（tensor的某一维度）上的的平均值，主要用作降维或者计算tensor（图像）的平均值。
#tf.clip_by_value主要是用来把张量中的数值限定在一个范围中，这样可以避免计算中的一些错误 比如log0
#这里采用损失函数是交叉熵损失，理解为用q(x)来衡量p(x)的困难程度 
#在多分类问题中 cross_entropy+softmax = tf.nn.softmax_cross_entropy_with_logits(labels=y_,logits=y)
#二分类问题有简化函数 tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y_,logits=y)
#还可以定义mse=tf.reduce_mean(square(y_-y))

#二分类问题损失函数
cross_entropy = -tf.reduce_mean(y_*tf.log(tf.clip_by_value(y,1e-10,1.0))+
                                (1-y_)*tf.log(tf.clip_by_value(1-y,1e-10,1.0)))
#回归问题损失函数
#loss_less = 10
#loss_more = 1
#loss = tf.reduce_sum(tf.where(tf.greater(y,y_),(y-y_)*loss_less,(y_-y)*loss_more))

train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)
#train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

from numpy.random import RandomState
rdm = RandomState(1)
data_size = 128
X = rdm.rand(data_size,2)
#回归问题 构建x1+x2+随机噪声
#Y = [[x1+x2+rdm.rand()/10.0-0.05] for (x1,x2) in X]
#二分类问题虚构验标签数值
Y = [[int(x1+x2<1)] for (x1,x2) in X]

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    
    print(sess.run(w1))
    print(sess.run(w2))
    
    STEPS = 5000
    for i in range(STEPS):
        start = (i * batch_size) % data_size
        end = min(start+batch_size,data_size)
        if(i>15 and i<20):#这个地方其实还是不太理解，感觉重复了 到底batch是怎么取的？？？？？
            print('start is {0}, end is {1}'.format(start,end))
        sess.run(train_step,feed_dict={x:X[start:end],y_:Y[start:end]})
        if(i%1000==0):
            total_cross_entropy = sess.run(cross_entropy,feed_dict={x:X,y_:Y})
            print('after {0} iterations, the loss is {1}'.format(i,total_cross_entropy))
    
    print(sess.run(w1))
    print(sess.run(w2))

#使用tensorflow的collection管理正则化参数
import tensorflow as tf 

#weights = tf.constant([[1.,2.],[3.,4.]])
#with tf.Session() as sess:
#    print(sess.run(tf.contrib.layers.l1_regularizer(.5)(weights)))
#    print(sess.run(tf.contrib.layers.l2_regularizer(.5)(weights)))
    
def get_weight(shape,l):
    var = tf.Variable(tf.random_normal(shape),dtype=tf.float32)
    tf.add_to_collection('losses',tf.contrib.layers.l2_regularizer(l)(var))
    return var

x = tf.placeholder(dtype=tf.float32,(None,2),'input-x')
y_ = tf.placeholder(dtype=tf.float32,(None,1),'input-y')

batch_size = 8
layers_dimension = [2,10,10,10,10,1]
n_layers = len(layers_dimension)
cur_layer =x

in_dimention = layers_dimension[0]

for i in range(1,layers_dimension):
    out_dimension = layers_dimension[1]
    weight = get_weight([in_dimention,out_dimension],0.001)
    bias = tf.constant(0.1,shape=[out_dimension])
    
    cur = tf.nn.relu(tf.matmul(in_dimention,weight)+bias)
    in_dimention = layers_dimension[i]
    
mse = tf.reduce_mean(tf.square(y_-cur_layer))
tf.add_to_collection('losses',mse)
loss = tf.get_collection('losses')

