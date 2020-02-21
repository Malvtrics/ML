##如何使用np.meshgrid 主要用来解决坐标网格点太多时候显示的问题
import numpy as np
import matplotlib.pyplot as plt
x = np.array([[0,1,2],[0,1,2]])
y = np.array([[1,1,1],[0,0,0]])
plt.plot(x,y,color='red',marker='.',markersize=10,linestyle='-')#要求x,y维度相同，不然会报错
plt.grid=True
plt.show()

x1 = np.array([0,1,2]) #注意这里的x1,y1表示横纵坐标的列向量 已经不是上面的二维矩阵
y1 = np.array([0,1])
X1,Y1=np.meshgrid(x1,y1)
plt.plot(X1,Y1,color='red',marker='.',markersize=10,linestyle='-')
plt.grid=True
plt.show()

#接下来就是NB之处，对于需要大量的横纵坐标点
x2 = np.linspace(0,2000,20)
y2 = np.linspace(0,2000,10)
X2,Y2=np.meshgrid(x2,y2)
plt.plot(X2,Y2,color='red',marker='.',markersize=10,linestyle='')
plt.grid = True
plt.show()

##如何在柱状图上面显示数字
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_info = pd.read_csv('student-info.csv',sep=';')
df_score = pd.read_csv('student-score.csv',sep=';')
result = pd.merge(df_info,df_score,on=['ID'])
print(result.head())
result1 = result.groupby(['age']).aggregate({'G1':'mean','G2':'mean','G3':'mean'})
ax = result1.plot(figsize=(15,5),kind='bar',width=0.9)# figsize unit: inch

#print(type(ax))   #<class 'matplotlib.axes._subplots.AxesSubplot'>
#can get all the rects (24)
for p in ax.patches:
    text = str(round(p.get_height(),2))
    ax.annotate(text, (p.get_x()+0.02, p.get_height()+0.2))
    #print(p)
