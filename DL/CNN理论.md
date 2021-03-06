## 首先看清楚几个缩写 !!!
+ ANN artificial neural network 人工神经网络 
+ FNN feedforward 前馈神经网络 
+ CNN convolutional 卷积神经网络 
+ RNN recurrent 循环神经网络

## 为什么要用CNN? 
+ 1）过拟合 2）计算量
+ 以图像为例
+ 假设原始图像有256*256*3个像素的数据，粗略计算可能是10万，然后经过第一层神经元，如果神经元个数太少则无法表达原始丰富信息
+ 假设第一层有4096个神经元，那么参数有大概4亿 这么多的参数，训练之后是很可能过拟合的
+ 这么多的参数，现在都是放到GPU上，会有很大的计算量，消耗资源严重

## CNN包括哪些层？
+ input layer=>CONV layer=>activation layer=>pooling layer=>FC(full connection???全连接层) layer=>batch normalization(optional)
+ input layer=> 
  + 去均值 （回到坐标原点） 
    + 方式：比如AlexNet会把100w个 256*256*3 的矩阵在每一个矩阵上求均值
          + 比如VGG会在每一个颜色通道上求均值
  + 归一化 （长度归一化为1）=   白化 whitened data
  + 去相关 decorrelated data 通过PCA变成正交向量 
  + 对图像数据一般只做去均值处理，因为RGB数据本来就已经都统一在0-256的幅度
  
+ CONV layer=>
  + 图像之间有关联性,所以每个神经元不需要和所有的图像块做全连接，只要和每个图像块做局部连接就行，所以有了 感受野的概念
  + receptive filed = 窗口 = 用来表示网络内部的不同位置的神经元对原图像的感受范围的大小
  + depth = 深度 = 神经元个数 理解：每个神经元都会得到一层图像(feature map) 图像的层数=深度
  + stride = 步长 = 窗口滑动多少格
  + zero-padding 得到的feature map可能是对应到一个值 维度、数量会变小 最后就收缩没了，所以要用0填充（注意这里是给原来数据填充0以满足滑窗）
  + 过程： 所有的滑窗先和第一个神经元（filter w0）做卷积 得到第一层
       + 所有的滑窗再和第二个神经元（filter w1）做卷积 得到第二层
       + w0可能捕捉的是图像的颜色  w1可能捕捉的是图像的轮廓 每个神经元都有各自的功能
  + 所以总结下来，每个神经元连接窗体的权重是一样的（参数共享性质） 每个神经元只关注一个特性 
  + 这样一组固定的权重和不同窗口内的数据做内积的过程 就是 卷积

+ activation layer=> 对卷积层的结果做非线性映射  
  + 常用的一些 老（sigmoid  tanh） 新（leaky-relu maxout relu elu）
  + 理解为什么老的会被淘汰： sigmoid 和 tanh在两侧无穷远时斜率为0 在CNN的链式求导中如果有一个映射求导为0 就挂了
  +（有一个猪队友导致梯度消失、梯度离散）
  + 建议先使用relu = rectified Linear Unit = 修正线性单元
  + 不行再用leaky-relu或者maxout
  + 某些情况tanh有不错效果 但是比较少
  
+ pooling layer=> 下采样来减小过拟合 max pooling / average pooling  取滑窗的均值还是最大值（最强特征）
  + 问题1：w权重参数是怎么定义出来的？
  + 问题2：max pooling 最强特征为什么等同于最大值？
 
+ fc layer=> 一般放在CNN尾部 用softmax 做分类或者 做回归
  + 如果放在其他层次 可能是做融合，使信息更加完善 
  + google2014 inception net中用全局池化代替全连接层，从那以后这个层可有可无 inception net 参考论文going deep with revolutions

##  CNN的损失函数？
+ 先看下GD BGD SGD
+ BGD(Batch Gradient Descent，批量梯度下降)：
+ SGD(Stochastic Gradient Descent，随机梯度下降)：仅仅选取一个样本j来求梯度。=> CNN 用这个
+ [简单代码实现参考](https://github.com/Malvtrics/ML/blob/master/%E5%87%A0%E7%A7%8D%E9%9A%8F%E6%9C%BA%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D%E8%AF%95%E9%AA%8C.py)

## CNN 优缺点？
+ 优
  + 共享卷积核 优化计算量 
  + 不用手选特征，自动训练权重  
  + 深层次网络抽取图像信息丰富，表达效果好
+ 缺
  + 需要调参，大样本数据量， GPU硬件依赖
  + 物理含义不明确，可解释性不强

## 梯度消失的本质原因？？？
+ sigmoid函数求导后在0处取得最大值1/4
<pre><code>import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10,10,200)
y = np.exp(-x) / pow((1+np.exp(-x)),2)
ax = plt.subplot(111)
ax.plot(x,y)
plt.show()</code></pre>
+ 通常初始化权重用均值为0标准差为1的高斯分布
+ 所以乘积永远都小于1/4

## CNN既然有先天缺陷，能替代吗？？？
+ [中文简介](https://baijiahao.baidu.com/s?id=1634461796649152771&wfr=spider&for=pc)
+ [英文详介](https://medium.com/ai%C2%B3-theory-practice-business/understanding-hintons-capsule-networks-part-i-intuition-b4b559d1159b)

## 如何解决梯度消失？？？
+ 激活函数
+ [BN](https://zhuanlan.zhihu.com/p/34879333)
  + 理解：通过对每一层的输出规范为均值和方差一致的做法，消除了反向传播因式中w带来的方法或者缩小的影响
  + 在论文中这个影响叫做 Internal Covariate Shift (由于网络中参数变化而引起内部结点数据分布发生变化的这一过程)
+ 残差网络
