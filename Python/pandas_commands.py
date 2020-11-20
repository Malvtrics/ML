import pandas as pd
import matplotlib.pyplot as plt

#参数说明: 文件路径 | 分隔符(默认是逗号) | 指定将哪一列作为索引 | 指定列的数据类型
df = pd.read_csv('path', delimiter=';', index_col=0, dtype={‘a’: np.float64, ‘b’: np.int32}) 

# 查看当前所有列的类型
df.dtypes

# 列的增删改查 
## 增加、查询略
## 精准删除
df = df.drop(['col1', 'col2'], axis=1)
## 模糊删除
df = df.loc[ : , ~df.columns.str.contains('Unnamed')]
df = df.loc[ : , ~df.columns.str.contains('^Unnamed')]
## 修改类型 
### pandas中的8种数据类型(object\int64\float64\bool\datetime64\timedelta[ns]\category->字符枚举)
df['cola'] = df['cola'].astype('category')
### 对于category类型如何转化成对应的code(int)
df['cola'] = df['cola'].cat.codes 
## 修改数据
df['a'].apply(函数名)
### 使用lambda时 elif需要多个if else嵌套
df['col1'] = df['col1'].apply(lambda x:1 if x=='HS' else (2 if x=='C' else 3))

# groupby语法 指定需要聚合的列 以及聚合过程中是否需要丢弃聚合列对应的空值
groupby = df.groupby(by=['colA','colB'],dropna=True) #返回一个groupby 对象
df1 = groupby.sum() #后面加聚合函数 返回dataframe 对象

# 取消索引 注意这里要把函数返回再赋给df
df = df.reset_index()

# plot结果，可以选择绘图类型 修改画布大小
df.plot(kind='bar',figsize=(15,10))
# 用bar的另外一种形式
df.plot.bar(x='col1',y='col2',figsize=(15,10))

# 简单plot两列 
x = df['a']
y = df['b']
plt.plt(x,y)

#dataframe如何转化为numpy array 
numpy_array = df.iloc[:,:6].to_numpy().reshape(4,5)
#numpy array转化为series 注意numpy array要转化成一维
series = pd.Series(numpy_array)
#series转化为dataframe
frame = { 'name1': series1, 'name2': series } 
df = pd.DataFrame(frame) 
