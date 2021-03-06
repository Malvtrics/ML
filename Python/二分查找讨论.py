def binary_search_recursion(lst,val,start,end):
    if(start>end):
        return None
    mid = (start+end)//2
    if(lst[mid]<val):
        return binary_search_recursion(lst,val,mid+1,end)
    if(lst[mid]>val):
        return binary_search_recursion(lst,val,start,mid-1)
    return mid

def binary_search_loop(lst, val):
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] < val:
            start = mid + 1
        elif lst[mid] > val:
            end = mid - 1
        else:
            return mid
    return None

import random as rd
import timeit

rd.seed(5)
lst = [rd.randint(1,100) for _ in range(500)]
lst.sort()
val = rd.choice(lst) #choice() 方法返回一个列表，元组或字符串的随机项。
print('val is {}'.format(val))

def test_recursion():
    return binary_search_recursion(lst,val,0,len(lst)-1)

def test_loop():
    return binary_search_loop(lst,val)

t1 = timeit.timeit('test_recursion',setup='from __main__ import test_recursion')
print('recursion:{}'.format(t1))
t2 = timeit.timeit('test_loop',setup='from __main__ import test_loop')
print('loop:{}'.format(t2))

import bisect
def binary_search_bisect(lst,val):
    i = bisect.bisect(lst,val)
    if i != len(lst) and lst[i] == val:
        return i
    return None

def test_bisect(lst,val):
    return binary_search_bisect(lst,val)

t3 = timeit.timeit('test_bisect',setup='from __main__ import test_bisect')
print('bisect:{}'.format(t3))

def test_index():
    return lst.index(val)

t4 = timeit.timeit("test_index()", setup="from __main__ import test_index")
print('index:{}'.format(t4))


val is 80
recursion:0.036648999999670195
loop:0.03477070000008098
bisect:0.018358499999521882
index:7.952047000000675


#######################################补充######################################
先说明的是，使用这个模块的函数前先确保操作的列表是已排序的。其插入的结果是不会影响原有的排序
接着看 bisect_left 和 bisect_right 函数，该函数用入处理将会插入重复数值的情况，返回将会插入的位置：
