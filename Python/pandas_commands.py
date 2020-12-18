import pandas as pd
import matplotlib.pyplot as plt

#参数说明: 文件路径 | 分隔符(默认是逗号) | 指定将哪一列作为索引 | 指定列的数据类型
df = pd.read_csv('path', delimiter=';', index_col=0, dtype={‘a’: np.float64, ‘b’: np.int32}) 
df = pd.read_excel('xxx.xlsx',sheet_name='xxx')
#初始化一个df 因为有时候文件不是csv或者excel 这时需要读取文件,比如已经从第一行读取20个列
df = pd.DataFrame([[None]*20],columns=cols)

# 查看当前所有列的类型
df.dtypes

# 列(行)的增删改查 

## 增加一行其实是新建一个df然后append上去,感觉比较蠢
df2 = pd.DataFrame(['val1','val2'...],columns=cols)
df.appen(df2)

## 删查同理
## 删除某(些)列
df = df.drop(['col1', 'col2'],axis=1)
df = df.dropna(how='any/all',axis=1) #空值类型
## 模糊删除 ~表示not df.loc[]
df = df.loc[ : , ~df.columns.str.contains('Unnamed')]
df = df.loc[ : , ~df.columns.str.contains('^Unnamed')]
## 可以使用各种条件筛选
df[df['column name'].map(len) < 2]

## 修改类型 
### pandas中的8种数据类型(object\int64\float64\bool\datetime64\timedelta[ns]\category->字符枚举)
df['cola'] = df['cola'].astype('category')
### 对于category类型如何转化成对应的code(int)
df['cola'] = df['cola'].cat.codes 
## 修改数据
df['a'].apply(函数名)
### 使用lambda时 elif需要多个if else嵌套
df['col1'] = df['col1'].apply(lambda x:1 if x=='HS' else (2 if x=='C' else 3))
### 如何使用col2更新col1 
### 举例：当col1包含abc时,col2为0,注意col1为None时不更新  第一个参数可以更新为其他条件 比如 df['col1']==2 
df.loc[df['col1'].str.contains('abc',na=False), 'col2'] = 0

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
