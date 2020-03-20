'''
基本的排序算法：冒泡 插入
常见排序算法：归并 快排(面试题40) 拓扑(主要用来解决依赖问题，比如abcde五门课的学习之间有依赖关系，最后决定学习顺序以顺利完成学业等)
其他排序算法 桶排序、堆排序
'''
def bubblesort(arr):
    for i in range(1,len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def insertionSort2(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
    return arr      
  
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
def mergeSort(arr,l,r): 
    if l < r:       
        m = int((l+(r-1))/2)
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 

#快速排序可以打印出具体变化
def partition(arr,low,high): 
    i = (low-1) 
    pivot = arr[high]     
    for j in range(low , high): 
        if arr[j] <= pivot: 
            #print('i=',i,';j=',j)
            i = i+1 
            #print('i=',i,';j=',j)
            #print(arr)
            arr[i],arr[j] = arr[j],arr[i] 
            #print(arr)
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    #print(arr)
    return (i+1) 
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

print(quickSort([3,1,7,4,5,2,8,6],0,7))
#快排的另外一种好理解的算法
def quicksort(arr):
    if len(arr) < 2:
        return arr
    mid = arr[len(arr)//2]
    left,right = [],[]
    arr.remove(mid)
    for i in arr:
        if i <= mid:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left)+[mid]+quicksort(right)
#掌握快排之后 做面试题40如鱼得水 https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
#可以轻松解决前k小问题
class Solution:
    def partition(arr,low,high):
        i = low-1
        pivot = arr[high]
        for j in range(low,high):
            if arr[j] < pivot:
                i += 1
                arr[i],arr[j]  = arr[j],arr[i]
        arr[high],arr[i+1] = arr[i+1],arr[high]
        return (i+1)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if len(arr) < k:
            return arr
        else: 
            low = 0
            high = len(arr)
            while(low < high):
                m = self.partition(arr, low, high)
                if m == k: 
                    break
                elif m > k:
                    high -= 1 
                else:
                    low = m + 1
        return arr[:k]
