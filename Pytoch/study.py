import torch
from torch.autograd import Variable

x = Variable(torch.Tensor(2,2)) #注意这里的T是大写,不是小写
print(x,x.grad) #pytorch的变量带有梯度信息

y = x + 2
print(y)

z = y * y * 3
#when you do loss.backward(), it is a shortcut for loss.backward(torch.Tensor([1])). This in only valid if loss is a tensor containing a single element.
out = z.mean()
print(out)

out.backward()
print(x.grad) #注意这里是6/4 为什么➗4，是因为算的均值，2*2一共有四个数

