#tf.truncated_normal tf.truncated_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None) 
#函数的为随机产生大小由shape指定的，均值默认为0，方差默认为1的正太分布，
#当产生数值偏离对称轴2个标准差时重新生成随机数，
#即产生的随机数x在(mean-2*stddev, mean+2*stddev)之间。 
#如果设置随机种子seed，那么相同的种子每次产生的随机数都相同。
#name是操作的名称
#tf.random_normal tf.random_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None) 
#参数含义与tf.truncated_normal相同，不同点在于对产生的落入(mean-2*stddev, mean+2*stddev)
#之外的随机数不会截断后重新生成。 
#代码部分参考了： 
#https://stackoverflow.com/questions/41704484/what-is-difference-between-tf-truncated-normal-and-tf-random-normal/41704789

import tensorflow as tf 
import matplotlib.pyplot as plt

n = 500000
A = tf.truncated_normal((n,))
B = tf.random_normal((n,))
with tf.Session() as sess:
    a, b = sess.run([A,B])

plt.hist(a, 100, (-4.2,4.2))
plt.hist(b, 100, (-4.2,4.2))
