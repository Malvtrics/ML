import pandas as pd
import matplotlib.pyplot as plt

#参数说明: 文件路径 | 分隔符(默认是逗号) | 指定将哪一列作为索引 | 指定列的数据类型
pd.read_csv('path', delimiter=';', index_col=0, dtype={‘a’: np.float64, ‘b’: np.int32}) 

# 删除 列名包含特定字符的列 的通用方法 (差别只是一个符号)
df = df.loc[ : , ~df.columns.str.contains('Unnamed')]
df = df.loc[ : , ~df.columns.str.contains('^Unnamed')]

# groupby语法 指定需要聚合的列 以及聚合过程中是否需要丢弃聚合列对应的空值
groupby = df.groupby(by=['colA','colB'],dropna=True) #返回一个groupby 对象
df1 = groupby.sum() #后面加聚合函数 返回dataframe 对象

# 取消索引 注意这里要把函数返回再赋给df
df = df.reset_index()

# 对某一列使用函数
df['a'].apply(函数名)

# plot结果，可以选择绘图类型 修改画布大小
df.plot(kind='bar',figsize=(15,10))

# 简单plot两列 
x = df['a']
y = df['b']
plt.plt(x,y)
