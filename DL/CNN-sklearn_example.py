import numpy as np
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

np.random.seed(0)
X,y = make_moons(200,noise=0.2)# 200个样本.noise表示有0.1的点是异常点
plt.scatter(x=X[:,0],y=X[:,1],s=10,c=y,cmap=plt.cm.Spectral)
#scatter用来画散点图
#s表示点的大小 c表示颜色，这里为什么0和1可以表示蓝色和橙色 查官方文档 如果是数字的时候，有个默认的颜色列表
#cmap采用什么用的colormap 不太理解这个 可能就是为了用不同的色彩
#plt.show()

def plot_decision_boundary(pred_func):
    x_min,x_max = X[:,0].min() - .5,X[:,0].max() + .5
    y_min,y_max = X[:,1].min() - .5,X[:,1].max() + .5
    h = 0.01
    
    #xx,yy = np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
    xx,yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    #####np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等，类似于pandas中的concat()
    #####np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等，类似于pandas中的merge()
    
    Z = pred_func(np.c_[xx.ravel(),yy.ravel()])#ravel->Return a contiguous flattened array.注意是[]使用
    Z = Z.reshape(xx.shape) #!!!注意又被这个地方坑了 Z.reshape()并没有改变原来的数组，需要赋值！！！
    
    #contour轮廓的意思 contourf 对等高线中间的区域进行颜色填充
    plt.contourf(xx,yy,Z,cmap=plt.cm.Spectral)
    plt.scatter(x=X[:,0],y=X[:,1],s=10,c=y,cmap=plt.cm.Spectral)

from sklearn.linear_model import LogisticRegressionCV
clf = LogisticRegressionCV()
clf.fit(X,y)

plot_decision_boundary(lambda x:clf.predict(x))
plt.title('logistic regression')
plt.show()

num_examples = len(X) #样本个数
nn_input_dim = 2 #输入的维度
nn_output_dim = 2 #输入的类别个数

#梯度下降参数
epsilon = 0.01 #学习率
reg_lambda = 0.01 #正则化参数

#定义损失函数
def calculate_loss(model):
    W1,b1,W2,b2 = model['W1'],model['b1'],model['W2'],model['b2']
    z1 = X.dot(W1)+b1
    a1=np.tanh(z1)
    z2 = a1.dot(W2)+b2
    #softmax先指数然后求权重
    exp_scores = np.exp(z2)
    #然后做归一化
    #理解：保持维度的np.sum哈哈哈
    #keepdims计算的时候保持维度，以便后面依然可以矩阵运算
    probs = exp_scores/ np.sum(exp_scores,axis=1,keepdims=2) 
    #损失函数 -log(标签*归一化概率) 由于标签只能是0和1 为0的项目都是0 其实目标是增大正样本猜测的概率
    correct_logprobs = -np.log(probs[range(num_examples),y])#???不理解 感觉可以换成下面 一会儿测试一下
    #correct_logprobs = -np.log(np.dot(probs,y))
    data_loss = np.sum(correct_logprobs)
    #加正则化项
    data_loss += reg_lambda/2 *(np.sum(np.square(W1))+np.sum(np.square(W2)))
    return 1./num_examples* data_loss

def build_model(nn_hdim,num_passes=20000, print_loss=False):
    #nn_hdim 隐层节点个数
    #num_passes 梯度下降迭代次数
    #print_loss if True 每1000次输出一次当前loss值
    
    np.random.seed(0)
    #用正态分布随机初始化，看来也不是那么随机，如何能在第一次随机的时候就能尽量靠近最终最优参数结果呢？？可以研究一下
    W1 = np.random.randn(nn_input_dim,nn_hdim)/np.sqrt(nn_input_dim)
    b1 = np.zeros((1,nn_hdim))
    W2 = np.random.randn(nn_hdim,nn_output_dim)/np.sqrt(nn_output_dim)
    b2 = np.zeros((1,nn_output_dim))
    
    model = {}
    
    for i in range(0,num_passes):
        z1 = X.dot(W1)+ b1
        a1 = np.tanh(z1)
        z2 = a1.dot(W2) + b2
        exp_scores = np.exp(z2)
        probs = exp_scores / np.sum(exp_scores,axis=1,keepdims=True)
        
        #反向传播 这里根据理论得到计算公式的步骤，直接一步一步来就行
        delta3 = probs
        delta3[range(num_examples),y] -= 1
        dW2 = (a1.T).dot(delta3)
        db2 = np.sum(delta3,axis=0,keepdims=True)
        delta2 = delta3.dot(W2.T)*(1-np.power(a1,2))
        dW1  = np.dot(X.T,delta2)
        db1 = np.sum(delta2,axis=0)
        
        #加上正则化项 
        #注意一般正则化考虑参数向量W 不考虑偏置项
        dW1 += reg_lambda * W1
        dW2 += reg_lambda * W2        
        
        #梯度下降更新
        W1 += -epsilon * dW1
        b1 += -epsilon * db1
        W2 += -epsilon * dW2
        b2 += -epsilon * db2
        
        model = {'W1':W1,'b1':b1,'W2':W2,'b2':b2}
        
        if print_loss and i%1000 == 0:
            print('Loss after iteration {} is {:.6f}'.format(i,calculate_loss(model)))
            
    return model
        
def predict(model,x):       
    W1,b1,W2,b2 = model['W1'],model['b1'],model['W2'],model['b2']
    z1 = x.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)    
    probs = exp_scores/np.sum(exp_scores,axis=1,keepdims=True)
    #得到的probs是两列 因为有两个output选择概率大的那个对应的类别
    #注意这里argmax的巧妙用法，输出列序号，刚好对应0和1
    return np.argmax(probs,axis=1)

model = build_model(3,print_loss=True)
plot_decision_boundary(lambda x:predict(model,x))
plt.title('Decision Boundary for hidden layer size 3')
plt.show()

#figsize : (float, float), optional, default: None
#width, height in inches.
plt.figure(figsize=(16,32))
hidden_layer_dimension = [1,2,3,4,5,20,50]
for i,nn_hdim in enumerate(hidden_layer_dimension):
    plt.subplot(4,2,i+1)#nrows, ncols, index 注意index 从1开始
    plt.title('Hidden layer size is {}'.format(nn_hdim))
    model = build_model(nn_hdim)
    plot_decision_boundary(lambda x: predict(model,x))
plt.show()
