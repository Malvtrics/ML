from sklearn import datasets
import numpy as np
import imp
iris = datasets.load_iris()

#print(type(iris))
#“bunch”: 一个简单的包含多个 “field” 的存储对象，
#可以方便的使用 python 中的 dict keys 或 object 属性来读取
#比如 target_names 包含了所请求的类别名称

#print(iris.target)
#print(iris.target_names)
#print(iris.data.shape)
#print(iris.target.shape)

a=iris.data
b=iris.target #b原来的shape是150个元素的一维数组，需要变成二维才能拼接
c=np.hstack((a,b.reshape(150,1)))

X = iris.data[:, [2, 3]]
y = iris.target
print('Class labels:', np.unique(y))

from sklearn.model_selection import train_test_split
#random_state的值相当于一种规则，通过设定为相同的数，每次分割的结果都是相同的
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.linear_model import Perceptron

#n_iter_int
#The actual number of iterations to reach the stopping criterion. 
#For multiclass fits, it is the maximum over every binary fit.

#eta0double
#Constant by which the updates are multiplied. Defaults to 1.
ppn = Perceptron(n_iter_no_change=40,eta0=0.1, random_state=0,max_iter=5)
print(ppn)#打印出perceptron的信息

ppn.fit(X_train, y_train)
print(ppn.coef_)#coef_是训练得到的模型参数
y_pred = ppn.predict(X_test)
print(y_pred)

'''
manifold模块

多维度数据集非常难于可视化。反而2维或者3维数据很容易通过图表展示数据本身的内部结构，等价的高维绘图就远没有那么直观了。
为了实现数据集结构的可视化，数据的维度必须通过某种方式降维。

最简单的降维手段是数据的随机投影。虽然这种方式实现一定程度的数据结构可视化，但是选择的随意性导致结果远不如意。
在随机投影中，更有趣的结构容易丢失。

为了解决这种问题，人们设计了一系列监督或非监督的线性降维框架，例如
Principal Component Analysis(PCA,主成分分析)
Independent Component Analysis（独立成分分析）
Linear Discriminant Analysis（线性判别分析）
…这些算法定义了特殊的评估量用于多维数据选择有趣的线性投影，这些手段是有效的，不过经常会错失数据结构中的非线性项。

Manifold Learing可以看作一种生成类似PCA的线性框架，不同的是可以对数据中的非线性结构敏感。
虽然存在监督变体，但是典型的流式学习问题是非监督的：它从数据本身学习高维结构，不需要使用既定的分类。

manifold.TSNE([n_components, perplexity, …])	t-distributed Stochastic Neighbor Embedding.	T-SNE
'''

'''
线性回归应用经验1
libsvm 一个c++ 的库，稀疏向量存储格式海量数据下单机速度还OK
高纬度离散化特征 准确率逼近非线性切分
参数调节比较方便
scikit learn中的LR是对libsvm的封装
经验2 spark MLlib
spark中有两个板块一个ml一个ml lib这两个板块中都有lr都可以完成并行化的优化

'''
'''
from sklearn.linear_model import LinearRegression
## kaggle旧金山犯罪问题 https://blog.csdn.net/GitzLiu/article/details/80212581
