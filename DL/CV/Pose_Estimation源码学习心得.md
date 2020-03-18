1. [source code](https://github.com/tensorboy/pytorch_Realtime_Multi-Person_Pose_Estimation)
2. args库
* [meavar给参数提供别名](https://blog.csdn.net/weixin_41803874/article/details/102586362)
* [parser.add_argument参数介绍](https://blog.csdn.net/Samaritan_x/article/details/84146029)
3. pillow库对图像做各种处理
4. 为啥在win上，train_VGG19中加入main函数才能运行而在linux上就不用?
* https://blog.csdn.net/AnyThingFromBigban/article/details/79835071
5. pytorch dataset类
* https://www.cnblogs.com/demo-deng/p/10623334.html 
* https://blog.csdn.net/sinat_42239797/article/details/93855728
```python
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
9. SGD中的momentum干啥的？？
* 与传统SGD相比，这个方法使得下降更具有方向性 原来是纵轴方向的震荡更大一些，现在我们在迭代的时候
* 考虑水平方向和纵轴方向的震荡，希望能够在水平方向上移动更快一些，这样可以快速趋向最佳点
*对比伪代码：
```python
dx = compute_gradient(x)
x += learning_rate * dx 
#sgd momentum 伪代码：
dx = compute_gradient(x)
vx = rho *  vx * dx 
x += learning_rate * vx 
```
10. __init__.py的作用？？
* 在文件夹中包含一个__init__.py，Python就会把文件夹当作一个package，里面的py文件就能够在外面被import了
11. yacs具体怎么配置的？？？
* 首先lib/config 文件夹里有__init__.py文件和default文件
* default 文件中 通过 `from yacs.config import CfgNode as CN` 定义节点
* [参考](https://blog.csdn.net/gefeng1209/article/details/90668882])
```python
from .default import _C as cfg
from .default import update_config
```
12. args.pin_memory是个什么鬼？？？
* 主机中的内存，有两种存在方式，一是锁页，二是不锁页，锁页内存存放的内容在任何情况下都不会与主机的虚拟内存进行交换（注：虚拟内存就是硬盘），
* 而不锁页内存在主机内存不足时，数据会存放在虚拟内存中。而显卡中的显存全部是锁页内存！
* 当计算机的内存充足的时候，可以设置pin_memory=True。当系统卡住，或者交换内存使用过多的时候，设置pin_memory=False。因为pin_memory与电脑硬件性能有关，
* pytorch 开发者不能确保每一个炼丹玩家都有高端设备，因此pin_memory默认为False。
13. [理解COCO数据集的标注格式](https://zhuanlan.zhihu.com/p/29393415)
14. [COCO数据集标注格式的segmentation里的ploygon和RLE具体都是什么??](https://www.zhihu.com/question/267996016)
15. [什么是 Amazon Mechanical Turk？](https://aws.amazon.com/cn/premiumsupport/knowledge-center/mechanical-turk-use-cases/)
16. [什么是RLE格式??](https://blog.csdn.net/wangdongwei0/article/details/83820869)
17. [adam算法刨根问底](https://blog.csdn.net/wfei101/article/details/79938305)
   + [算法参考](https://juejin.im/entry/5983115f6fb9a03c50227fd4)
   + 优化算法-> 一阶优化 + 二阶优化(太浪费资源，pass) -> 一阶优化 -> 梯度下降 -> 变种：SGD  MinibatchSGD 
   + 继续优化 -> 动量法(较小无关方向震荡) -> Nesterov梯度加速法 -> Adagrad -> AdaDelta -> Adam
   + [2019 新算法Adabound](https://medium.com/syncedreview/iclr-2019-fast-as-adam-good-as-sgd-new-optimizer-has-both-78e37e8f9a34#:~:text=SGD%20is%20a%20variant%20of,random%20selection%20of%20data%20examples.&text=Essentially%20Adam%20is%20an%20algorithm,optimization%20of%20stochastic%20objective%20functions.)



