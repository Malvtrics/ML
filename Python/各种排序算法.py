def quick_sort(arr):
    if(len(arr)<2):
        return arr
    mid = arr[len(arr)//2]
    left,right=[],[]
    arr.remove(mid)
    for item in arr:
        if(item>=mid):
            right.append(item)
        else:
            left.append(item)
    return quick_sort(left)+[mid]+quick_sort(right)

quick_sort([1,4,2,6,0,1,-4,17,11,12,-23])

#one line version
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([
     item for item in array[1:] if item <= array[0]
 ]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
 
quick_sort([2,5,9,3,7,1,5])
