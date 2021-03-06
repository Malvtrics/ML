Series:One-dimensional ndarray with axis labels (including time series).
Construction:class pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
          data : array-like, Iterable, dict, or scalar value->Contains data stored in Series.
eg1:Series(ndarray,index = [id1,id2,id3])
eg2:Series([1,2,3],index = [id1,id2,id3])

value_counts()  #Return a Series containing counts of unique values.->NaN exclued as default

child_series = s[[col1,col2,col3]]
Series.loc
Access a group of rows and columns by label(s) or a boolean array.
.loc[] is primarily label based, but may also be used with a boolean array.
Allowed inputs are:
A single label, e.g. 5 or 'a', (note that 5 is interpreted as a label of the index, and never as an integer position along the index).
A list or array of labels, e.g. ['a', 'b', 'c'].
A slice object with labels, e.g. 'a':'f'.
A boolean array of the same length as the axis being sliced, e.g. [True, False, True].
A callable function with one argument (the calling Series or DataFrame) and that returns valid output for indexing (one of the above)



##从dataframe中取符合条件的数据输出series 然后用values输出ndarray
#known_age = age_df[age_df.Age.notnull()].values
#unknown_age = age_df[age_df.Age.isnull()].values
#y = known_age[:,0]
#x = known_age[:,1:]
#rfr = RandomForestRegressor(random_state=0,n_estimators=2000,n_jobs=-1)
#rfr.fit(x,y)
#predicted_ages = rfr.predict(unknown_age[:,1:])
#data.loc[(data.Age.isnull()),'Age'] = predicted_ages
##print(data.Age)

#做特征转化的典型例子 性别本来是一个特征，但是如果做线性回归的话 要展开两个特征 然后分析权重
dummies_sex = pd.get_dummies(data['Sex'],prefix='sex')
print(dummies_sex)
new_data = pd.concat([data,dummies_sex],axis=1) #注意默认是行廉洁，要加axis
new_data.drop(['Sex'],axis=1,inplace=True)
#用法：DataFrame.drop(labels=None,axis=0, index=None, columns=None, inplace=False)
#
#参数说明：
#labels 就是要删除的行列的名字，用列表给定
#axis 默认为0，指删除行，因此删除columns时要指定axis=1；
#index 直接指定要删除的行
#columns 直接指定要删除的列
#inplace=False，默认该删除操作不改变原数据，而是返回一个执行删除操作后的新dataframe；
#inplace=True，则会直接在原数据上进行删除操作，删除后无法返回。
#
#因此，删除行列有两种方式：
#1）labels=None,axis=0 的组合
#2）index或columns直接指定要删除的行或列
print(new_data.head())

import pandas as pd
import numpy as np
from numpy import nan as NA
from pandas import DataFrame, Series
from matplotlib import pyplot as plt

#%matplotlib inline
#obj = Series([4,7,-5,3])
#print(obj)
#obj2 = Series([4,7,-5,3],index=['a','b','c','d'])
#print(obj2['a'])
#
#print('b' in obj2)
#print(obj2[obj2>0]) 
#
#print(np.exp(obj))
#
#status = ['e','a','b','c']
#obj3 = Series(obj2,index=status)
#print(obj3)
#
#print(pd.isnull(obj3))

#
#obj = Series(['Bob','Steven','Linq','Spanish'], index = ['China','US','Shit','Xcode'])
#obj2 = obj.reindex(['US','China','Shit','Xcode','Emmy','Long'],fill_value = 0) #可以用于对缺失值进行填充
#print(obj2)
#
#obj3 = Series(['blue','red','purple','green'], index=[0,2,4,6])
#obj4 = obj3.reindex(range(10),method='ffill') #forward fill利用前面的值填充
#print(obj4)
#
#obj3.sort_index()
#obj3.sort_values()
#
##DataFrame和Series里面的切片是引用的, 所以比正常使用数组效率要高？？？为什么要这么设计？
#obj = Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#x = obj[1:2]
#x[1] = 100
#print(x)
#
##通过索引访问时时全闭的
#x = obj['a':'c']  #1,2,3


####################################################DataFrame#########################################

#pandas frame 模块从操作角度考虑 设置为列优先，通常情况下都是行优先

data = {'city':['beijing','shanghai','guangdong','datong','guangling'], 
        'year':[2016,2017,2018,2019,2020], 
        'GDP':[2030.5,44321.09,31243.43,4310.431,43243.88]}
frame = DataFrame(data, columns=['year','city','GDP','delt'])
frame.set_index('year')
#print(frame.city)
#print(frame['year'])

#print(frame,'\n')
#print(frame.iloc[1,],'\n') #访问第一行
#print(frame.iloc[:,2],'\n') #访问第二列
#print(frame.iloc[1:3,1:2],'\n')#切片访问第一二行 第一列
#print(frame.loc[1,'city']) #loc使用户可以通过名字访问

frame['debt'] = Series([-1.2,-1.5,-1.8,-1.7],index = [0,1,2,4])
#print(frame)

frame['pool'] = (frame['debt']<-1.6)
#print(frame) #在特征工程中用的多，可以轻松赋值 0 1

data = DataFrame(np.arange(-5,11).reshape([4,4]),
                 index = ['Ohio','Colorado','Utah','New York'],
                 columns = ['one','two','three','four'])
#print(data)
#print(data.drop(['Colorado','Ohio']))
#print(data.drop('two',axis = 1))
#print(data.drop(['two','four'],axis = 1))
#print(data.loc[data.three>10])

data[data>10] = 0
#print(data)
#print(data+100)

s = data.iloc[0]
#print(s)
#print(data-s) #每一行减去对应的s的值
s2 = data.three
#print(data.sub(s2,axis = 0))

#print(np.abs(data))

f = lambda x:x.max()-x.min()
#print(data.apply(f))
#print(data.apply(f,axis=1))

def f2(x):
    return Series([x.min(),x.max()],index = ['min','max'])
#print(data.apply(f2))
#print(data.apply(f2,axis=1))

data = data + 0.347
#print(data)
format1 = lambda x: '%.2f' % x
#print(data.applymap(format1))
#print(data['four'].map(format1))

#print(data.sort_index())
#print(data.sort_index(axis=1,ascending=False))

df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],index=['a', 'b', 'c', 'd'],columns=['one', 'two'])
#print(df,'\n')
#print(df.sum(),'\n')
#print(df.cumsum(),'\n')
#print(df.describe(),'\n')


df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'],'data2': range(3)})
#print(df1)
#print(df2)
#print(pd.merge(df1,df2))
#print(pd.merge(df1,df2,on='key'))


df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})
df4 = DataFrame({'rkey': ['a', 'b', 'd'],'data2': range(3)})
#print(df3)
#print(df4)
#print(pd.merge(df3,df4))
#print(pd.merge(df3,df4,left_on='lkey',right_on='rkey'))
#print(pd.merge(df1,df2,how='outer'))

left = DataFrame({'key': ['foo', 'foo', 'bar'],
                  '_key': ['one', 'two', 'one'],
                  'val': [1, 2, 3]})
right = DataFrame({'key': ['foo', 'foo', 'bar', 'bar'],
                   '_key': ['one', 'one', 'one', 'two'],
                   'val': [4, 5, 6, 7]})
#print(left)
#print(right)
#print(pd.merge(left, right, on=['key', '_key'], how='outer')) # 基于多个列的合并"
#print(pd.merge(left, right, on='key', suffixes=('_left', '_right'))) # 重名列可以指定合并后的后缀"

left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
#print(left1)
#print(right1)
#print(pd.merge(left1, right1, left_on='key', right_index=True)) # 使用right的索引参与合并"

left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                  index=['a', 'c', 'e'],
                  columns=['Ohio', 'Nevada'])
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                   index=['b', 'c', 'd', 'e'],
                   columns=['Missouri', 'Alabama'])
#print(left2)
#print(right2)
#print(left2.join(right2, how='outer')) # join默认使用索引合并"

another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                    index=['a', 'c', 'e', 'f'],
                    columns=['New York', 'Oregon'])
#print(left2.join([right2, another])) # 一次合并多个DataFrame，默认使用全连接。"

s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])
#print(pd.concat([s1, s2, s3],axis=1,sort=False)) # 默认沿着行的方向连接"


a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b = Series(np.arange(len(a), dtype=np.float64),
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan
#print(a)
#print(b)
#print(np.where(pd.isnull(a), b, a)) # 根据where筛选，如果a对应位置的元素为None就选b"

df1 = DataFrame({'a':[1,NA,5,np.NAN],
                 'b':[NA,2,np.nan,6],
                 'c':range(2,18,4)})
df2 = DataFrame({'a':[5,4,np.nan,3,7],
                 'b':[NA,3,4,6,8]})
#print(df1)
#print(df2)
#print(df1.combine_first(df2))
    
#其他需要的知识点\n",
#1. pivot和melt\n",
#2. 值替换\n",
#3. 数据切割\n",
#4. 排列组合和随机采样"
    
# Pandas绘图


import pandas as pd
#test1
data=pd.read_csv('NVDA.csv', index_col='Date', parse_dates=['Date'])
data['year'] = data.index.year
print(data.info())
#test2
data1=pd.read_csv('NVDA.csv')
data1.set_index(['Date'],inplace=True)
data1.index = pd.to_datetime(data1.index)
#data1['Date'] = pd.to_datetime(data1['Date'])
data1['year'] = data1.index.year
print(data1.info())

#注意一但某一列被设置成索引后，不能通过data1['Date'] = pd.to_datetime(data1['Date'])这种方式来改类型 
需要通过data1.index = pd.to_datetime(data1.index)来改类型
所以最好就是test1中在开始读取的时候就设置好索引，尤其是时间列索引的解析
