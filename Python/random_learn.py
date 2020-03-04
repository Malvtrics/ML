首先都是左闭右开

python自带的random 返回一个小数或者一个整数 没有维度概念
random.random() #0.15543373681847383
random.randint(1,50)  #37

#randrange = one random integer in the range
random.randrange(100) #78
random.randrange(70,100) #89
random.randrange(2,4,1) #3 #start end step 

numpy中的random
np.array([2,3,4])
np.arange(6).reshape(2,3) # 从0到5 两行三列

np.random.rand() #0.10248419513306517
np.random.rand(2) # array([0.95513625, 0.40830807])
np.random.rand(2,3) #均匀分布 [0,1)之间 两行三列 #array([[0.44542152, 0.0484066 , 0.77979728], [0.7308293 , 0.79195275, 0.70368762]])

#randn N(0,1)
np.random.randn()：#2.3507557480531194
np.random.randn(2) #array([ 0.60471507, -1.19679745])
np.random.randn(2,3) #array([[-0.96738554,  0.77820108,  1.84241556],[ 0.36377721, -0.16803053, -1.78429077]])

np.random.randint(10) #6 
np.random.randint(0,3) #0/1/2 指定size的时候可以变成多维，默认是一个数
np.random.randint(low=1, high=4, size=4, dtype='l')  #array([1, 3, 2, 2]) 
np.random.randint(low=1, high=4, size=(2,2), dtype='l')  #array([[1, 2],[1, 3]])
