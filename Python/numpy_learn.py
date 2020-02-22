import numpy as np
import matplotlib.pyplot as plt

arr = np.array([[1,2,3],[4,5,6]]) #初始化
arr_sum = arr.T + np.ones((3,2),dtype='int32') 

x = np.linspace(0,2*np.pi,50) #不要写成linespace
y = np.sin(x)
plt.plot(x,y,'b')
plt.show() #注意在cmd下需要加上这一句才能显示出来

arr2 = np.arange(12).reshape(3,4)

#连续均匀分布 设汽通过某站的汽车每10min 一辆那么乘客候车的时间是在[0.10] 上服从均匀分布
#离散均匀分布 掷骰子
设汽通过某站的汽车每10min 一辆那么乘客候车的时间是在[0.10] 上服从均匀分布的
官方例子：
s = np.random.uniform(-1,0,1000)
count, bins, ignored = plt.hist(s, 15, normed=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.show()

n1 = np.array([1,2,3])
n1.shape  #class member if one dimension then only display count of elements (3,) using turple type
n2 = np.linspace(1,100,3) #contains start and end, 等差数列  步长是 (end-start)/(count-1)
n3 = np.empty((6,6)) 
n4 = np.eye(4)
n5 = np.random.randn(3,4) #rand 平均分布 randn 正态分布
n5 = np.random.randn(4,8)
n5.fill(7) 
n6 = np.arange(10)
np.random.shuffle(n6) #洗牌 注意用法 不需要另外赋值
n8 = np.zeros(4)
n8 = np.zeros((4,5)) #param is turple
n9 = np.ones((6,7)) 
n10 = np.ones_like(n9)  # all one but the shape is the same as n9
n11 = np.round(n2,2)
n12 = n11.astype(np.float32)
print(n12.size)
print(n12.ndim) 
print(n12.dtype)
n13 = np.ones([3,4,5]) # 3 dimentional array
# print(n4[1,1:])
# print(n4[1,[0,2]]
# bool_a = n13 > 5
# print(bool_a)
# print(n13[bool_a])
# 有一个地方讲的不对 arr[1,2] 和 arr[[1],2] 找出的结果都是一样的， 不同的是一个返回一个数，另外一个返回一个数组
n14 = n13.reshape(2,2,3) #2d to 3d
arr = np.arange(8)
arr.shape = 1,8
#print(arr)
arr = np.random.randn(2,3)
arr2 = arr.transpose()
arr2 = arr.T

arr3 = arr.flattern()
np.sum(arr,axis=0) #表示消除第一个维度 （行） 所以是按列加和
np.sort(arr,axis=1)
np.reshape(arr,(5,-1))
a,b = np.hsplit(arr2,2)

arr.repeat([2,3,4]) #第一个元素重复2次 第二个3次 第三个4次
arr.repeat([1,2,3,4],axis=0)
np.tile(arr,2)
np.tile(arr,(2,3))

np.save('C:\\Users\\mengwang\\Desktop\\GPMA\\Other\\Python\\a1',arr) #注意要用双斜线 不然会报错

x = np.array([[1, 2, 3], [4, 5, 6]])
np.ravel(x)
#array([1, 2, 3, 4, 5, 6])
#It is equivalent to reshape(-1, order=order).
