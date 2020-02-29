Fisher-Yates Shuffle
思路：从原始数据中随便抽一个数字到新数组中
import random 
def fisher_yates_shuffle(list):
  res = []
  while(list):
    p=random.randrange(len(list))
    res.append(list[p])
    list.pop(p)
   return res
  
Knuth-Durstenfeld Shuffle
思路：对上面算法的改进，每次从未处理的数据中随机取出一个数字，然后放在数组的末尾，原地打乱
import random
def knuth_shuffle(list):
    # no extra space
    for i in range(len(list) - 1, 0, -1):
        p = random.randrange(0, i + 1)
        list[i], list[p] = list[p], list[i] #注意python的变量交换
    return list
    
Inside-Out Algorithm
Knuth算法是一个in-place算法，原始数据被直接打乱，但有些情形下需要保存原始数据，因此需要重新开辟一个新数组来存储打乱后的序列。
Inside-Out算法的基本思想是设置一个游标 i 从前向后扫描原始数据的拷贝，在[0, i]之间随机一个下标 j，然后用位置 j 的元素替换掉位置 i 处的数字，
再用原始数据位置 i 的元素替换掉拷贝数据位置 j 的元素。作用相当于在拷贝数据中交换位置 i 和 j 处的值
import random
def inside_out_shuffle(list):
    # save original data
    res = list[:]
    for i in range(1, len(list)):
        j = random.randrange(0, i)
        res[i] = res[j]
        res[j] = list[i]
    return res
    
  python内部random.shuffle用的是第二种方法
