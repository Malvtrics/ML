#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import exp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


# In[2]:


def create_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data,columns=iris.feature_names)
    df['label']=iris.target
    df.columns = ['sepal length','sepal width','petal length','petal width','label']
    data = np.array(df.iloc[:100,[0,1,-1]])
    return data[:,:2],data[:,-1]


# In[3]:


x,y=create_data()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
# 这里test_size 取 0.25的时候 准确率是0.96 


# In[4]:


class logistic_classifier:
    def __init__(self,max_iter=200,lr=0.01):
        self.max_iter=max_iter
        self.lr = lr
    def sigmoid(self,x):
        return 1/(1+exp(-x))
    def data_matrix(self,x):
        data_mat=[]
        for d in x:
            data_mat.append([1.0,*d]) #这里的1是偏置
            # 知识点：用函数时，*可以使用运算符将**可迭代对象解压缩为函数调用中的参数：
            # eg : d -> [1.0,3.4] *d -> 1.0 3.4
        return data_mat
    def fit(self,x,y):
        data_mat = self.data_matrix(x)
        self.weights = np.zeros((len(data_mat[0]),1),dtype=np.float32) ## 3 * 1
        for _ in range(self.max_iter):
            for i in range(len(x)):
                result = self.sigmoid(np.dot(data_mat[i],self.weights))
                error = y[i]-result  #注意这里结合公式的正负号
                self.weights += self.lr*error*np.transpose([data_mat[i]])
        print("logistic lr:{},max iter:{}".format(self.lr,self.max_iter))
    def score(self,x_test,y_test):
        x_test = self.data_matrix(x_test)
        right = 0 
        for x,y in zip(x_test,y_test):
            result = np.dot(x,self.weights)
            if(result>0 and y==1 ) or (result<0 and y==0):
                right+=1
        return right/len(x_test)


# In[5]:


lr_clf=logistic_classifier()
lr_clf.fit(x_train,y_train)
lr_clf.score(x_test,y_test)


# In[6]:


x_points = np.arange(4,8)
#横轴x1 纵坐标x2 
# 截平面 w1x1+w2x2+b=0 
# x2 = -(w1x1+b)/w2
y_ = -(lr_clf.weights[1]*x_points+lr_clf.weights[0])/lr_clf.weights[2]
plt.plot(x_points,y_)
plt.scatter(x[:50,0],x[:50,1],label='0')
plt.scatter(x[50:,0],x[50:,1],label='1')
plt.legend()


# In[7]:


import matplotlib.pyplot as plt 
import numpy as np
from sklearn import datasets, linear_model,  model_selection


# In[8]:


def load_data():
    iris = datasets.load_iris()
    x_train = iris.data
    y_train = iris.target
    return model_selection.train_test_split(x_train, y_train, test_size=0.25, random_state=0)


# In[9]:


data = load_data()


# In[10]:


def test_logistic_regression(data):
    x_train,x_test,y_train,y_test=data
    regr = linear_model.LogisticRegression()
    regr.fit(x_train,y_train)
    print("coefficient:{},intercept:{}".format(regr.coef_,regr.intercept_))
    print("socre:{}".format(regr.score(x_test,y_test)))


# In[11]:


test_logistic_regression(data)


# In[12]:


def test_logistic_regression_multinomial(data):
    x_train,x_test,y_train,y_test=data
    regr = linear_model.LogisticRegression(multi_class="multinomial",solver="lbfgs")
    regr.fit(x_train,y_train)
    print("coefficient:{},intercept:{}".format(regr.coef_,regr.intercept_))
    print("socre:{}".format(regr.score(x_test,y_test)))


# In[13]:


test_logistic_regression_multinomial(data)


# In[14]:


def test_logistic_regression_c(data):
    x_train,x_test,y_train,y_test=data
    cs = np.logspace(-2,4,num=100)
    scores = []
    for c in cs:
        #正则化系数λ的倒数，float类型，默认为1.0。必须是正浮点型数。像SVM一样，越小的数值表示越强的正则化。
        regr = linear_model.LogisticRegression(C=c,solver="liblinear",multi_class="ovr")
        regr.fit(x_train,y_train)
        scores.append(regr.score(x_test,y_test))
    print(scores[-1])
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(cs,scores)
    ax.set_xlabel('c')
    ax.set_ylabel('score')
    ax.set_xscale('log')
    ax.set_title('logregression_c')
    plt.show()


# In[15]:


test_logistic_regression_c(data)

