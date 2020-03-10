1. [source code](https://github.com/tensorboy/pytorch_Realtime_Multi-Person_Pose_Estimation)
2. args库
	+ [meavar给参数提供别名](https://blog.csdn.net/weixin_41803874/article/details/102586362)
	+ [parser.add_argument参数介绍](https://blog.csdn.net/Samaritan_x/article/details/84146029)
3. pillow库对图像做各种处理
4. 为啥在win上，train_VGG19中加入main函数才能运行而在linux上就不用?
	+ https://blog.csdn.net/AnyThingFromBigban/article/details/79835071
5. pytorch dataset类
	+ https://www.cnblogs.com/demo-deng/p/10623334.html 
	+ https://blog.csdn.net/sinat_42239797/article/details/93855728
```
import torch
import torch.utils.data as d
batch_size = 4
x = torch.linspace(1,10,10)
y = torch.linspace(10,1,10)
torch_dataset = d.TensorDataset(x,y)
loader = d.DataLoader(dataset=torch_dataset,batch_size=batch_size,shuffle=True,num_workers=2,drop_last=True)
print(enumerate(loader))
def show_batch():
    for epoch in range(3):
        for step, (batch_x,batch_y) in enumerate(loader):
            #training:
            print('epoch:{},step:{},batch_x:{}，batch_y:{}'.format(epoch,step,batch_x,batch_y))
show_batch()
```
6. train的时候数据做shuffle,val的数据集不做shuffle
7. python中collection库中的有序字典类[OrderdDict](https://www.cnblogs.com/notzy/p/9312049.html)
8. [pytorch request_grad属性](https://zhuanlan.zhihu.com/p/85506092)
9. sgd + momentum (可以控制参数是否要momentum)
	+ 与传统SGD相比，这个方法使得下降更具有方向性 原来是纵轴方向的震荡更大一些，现在我们在迭代的时候
	+ 考虑水平方向和纵轴方向的震荡，希望能够在水平方向上移动更快一些，这样可以快速趋向最佳点
	+对比伪代码：
```
dx = compute_gradient(x)
x += learning_rate * dx 
sgd momentum 伪代码：
dx = compute_gradient(x)
vx = rho *  vx + dx 
x += learning_rate * vx 
```
10. __init__.py的作用？？
	+ 在文件夹中包含一个__init__.py，Python就会把文件夹当作一个package，里面的py文件就能够在外面被import了
11. yacs具体怎么配置的？？？
	+ 首先lib/config 文件夹里有__init__.py文件和default文件
```
from .default import _C as cfg
from .default import update_config
```
	+ default 文件中 通过 `from yacs.config import CfgNode as CN` 定义节点
	+ [参考](https://blog.csdn.net/gefeng1209/article/details/90668882])

