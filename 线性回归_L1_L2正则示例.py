#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt 
from sklearn import model_selection, datasets, linear_model


# In[13]:


def load_data():
    diabets = datasets.load_diabetes()
    return model_selection.train_test_split(diabets.data, diabets.target,test_size=0.25,random_state=1)


# In[16]:


def test_linear(data):
    x_train,x_test,y_train,y_test=data
    regr = linear_model.LinearRegression()
    regr.fit(x_train,y_train)
    print("coefficients:",regr.coef_,",",regr.intercept_)
    print("err:",np.mean(regr.predict(x_test)-y_test)**2)
    print("score:",regr.score(x_test,y_test))


# In[34]:


data = load_data()
test_linear(data)


# In[32]:


def test_lasso(data):
    x_train,x_test,y_train,y_test=data
    regr = linear_model.Lasso()
    regr.fit(x_train,y_train)
    print("coefficients:",regr.coef_,",",regr.intercept_)
    print("err:",np.mean(regr.predict(x_test)-y_test)**2)
    print("score:",regr.score(x_test,y_test))


# In[40]:


data = load_data()
test_lasso(data)


# In[58]:


def test_lasso_alpha(data):
    x_train,x_test,y_train,y_test=data
    alphas=[0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100,200,500,1000]
    scores = []
    for i,alpha in enumerate(alphas):
        regr = linear_model.Lasso(alpha=alpha)
        regr.fit(x_train,y_train)
        scores.append(regr.score(x_test,y_test))
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(alphas,scores)
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel("score")
    ax.set_xscale("log") #这里竟然有这么一个牛逼操作。。。
    ax.set_title("lasso")
    plt.show ()


# In[59]:


test_lasso_alpha(data)


# In[50]:


def test_ridge(data):
    x_train,x_test,y_train,y_test=data
    regr = linear_model.Ridge()
    regr.fit(x_train,y_train)
    print("coefficients:",regr.coef_,",",regr.intercept_)
    print("err:",np.mean(regr.predict(x_test)-y_test)**2)
    print("score:",regr.score(x_test,y_test))


# In[51]:


test_ridge(data)


# In[60]:


def test_ridge_alpha(data):
    x_train,x_test,y_train,y_test=data
    alphas=[0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100,200,500,1000]
    scores = []
    for i,alpha in enumerate(alphas):
        regr = linear_model.Ridge(alpha=alpha)
        regr.fit(x_train,y_train)
        scores.append(regr.score(x_test,y_test))
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(alphas,scores)
    ax.set_xlabel("alpha")
    ax.set_ylabel("score")
    ax.set_xscale("log")
    ax.set_title("lasso")
    plt.show ()


# In[61]:


test_ridge_alpha(data)

