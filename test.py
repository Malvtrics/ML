#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import scipy as sp
from scipy.optimize import leastsq
#最小二乘函数做拟合
import matplotlib.pyplot as plt


# In[2]:


def real_func(x):
    return np.sin(2*np.pi*x)


# In[3]:


def fit_func(p,x):
    #多项式函数
    f =  np.poly1d(p) #np.poly1d返回的是一个表示多项式的对象
    return f(x) 


# In[4]:


def residuals_func(p,x,y):
    ret = fit_func(p,x) -  y 
    return ret


# In[5]:


x = np.linspace(0,1,10)
x_point = np.linspace(0,1,1000)
y_ = real_func(x)
y = [np.random.normal(0,0.1)+y1 for y1 in y_]


# In[6]:


def fitting(M):
    p_init = np.random.rand(M+1)
    #func 是我们自己定义的一个计算误差的函数，
    #x0 是计算的初始参数值  随便定义，但是如何定义会去影响求解速度
    #args 是指定func的其他参数
    #返回的第一个参数是 拟合好的 ndarray
    p_lsq = leastsq(residuals_func,p_init,args=(x,y))
    print("fitting parameters:",p_lsq[0])
    plt.plot(x_point,real_func(x_point),label="real")
    plt.plot(x_point,fit_func(p_lsq[0],x_point),label="fitted curve")
    plt.plot(x,y,'bo',label="noise") #绘制10个采样点 一定是包含了误差
    plt.legend()
    return p_lsq


# In[7]:


p_lsq_9 = fitting(9)


# In[8]:


regulization = 0.001


# In[9]:


def residual_regulization(p,x,y):
    ret = fit_func(p,x) -  y 
    ret = np.append(ret, np.sqrt(0.5*regulization*np.square(p)))
    return ret


# In[10]:


p_init = np.random.rand(10)
p_lsq_reg = leastsq(residual_regulization,p_init,args=(x,y))
plt.plot(x_point,real_func(x_point),label="real")
plt.plot(x_point,fit_func(p_lsq_9[0],x_point),label="fitted curve")
plt.plot(x_point,fit_func(p_lsq_reg[0],x_point),label="regulization")
plt.plot(x,y,'bo',label="noise") #绘制10个采样点 一定是包含了误差
plt.legend()

