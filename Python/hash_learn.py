处理哈希冲突的几种方法：

开放定址法
开放定址法就是产生冲突之后去寻找下一个空闲的空间，其中又包括下面两种：
线性探测法：di= i ，或者其他线性函数。相当于逐个探测存放地址的表，直到查找到一个空单元，然后放置在该单元。
平方探测法：（https://python123.io/index/topics/data_structure/hash_table）

链表法
这是另外一种类型解决冲突的办法，散列到同一位置的元素，不是继续往下探测，而是在这个位置是一个链表，这些元素则都放到这一个链表上。

再散列
如果一次不够，就再来一次，直到冲突不再发生。

建立公共溢出区
将哈希表分为基本表和溢出表两部分，凡是和基本表发生冲突的元素，一律填入溢出表(注意：在这个方法里面是把元素分开两个表来存储)。

下面是常用链表法实现的源码，加深哈希表的理解

hash_table= [None] * 10

def hash_func(key):
    return key % len(hash_table)

def insert(hash_table,key,value):
    hash_key = hash_func(key)
    hash_table[hash_key] = value
    
insert(hash_table,10,'Martin')
insert(hash_table,25,'Iulian')
insert(hash_table,35,'Adriana')
print(hash_table) #due to collision, we can't see Iulian there

#resolve such collision
hash_table = [[] for _ in range(10)]
print(hash_table)

def insert(hash_table,key,value):
    hash_key = hash_func(key)
    hash_table[hash_key].append(value)

insert(hash_table,10,'Martin')
insert(hash_table,25,'Iulian')
insert(hash_table,35,'Adriana')
print(hash_table) #due to collision, we can't see Iulian there

#Python’s built-in “hash” function is used to create a hash value of any key. 
#This function is useful as it creates an integer hash value for both string and integer key. 
#The hash value for integer will be same as it is, i.e. hash(10) will be 10, hash(20) will be 20, and so on.
#In the below code, note the difference in output while using 10 and ’10’. 
#10 (without quote) is treated as an integer and ’10’ (with quote) is treated as a string.

print(hash('xyz'))
print(hash('10'))
print(hash(10))

hash_table = [[] for _ in range(10)]
#so we replace our own hash_func with hash
def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]   
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True 
            break
    if key_exists:
        bucket[i] = ((key, value))#note: i can be find in the lastest scope
    else:
        bucket.append((key, value))

insert(hash_table,10,'Martin')
insert(hash_table,25,'Iulian')
insert(hash_table,35,'Adriana')
print(hash_table)

def search(hash_table,key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i,kv in enumerate(bucket):
        k,v = kv
        if(k==key):
            return v
print(search(hash_table,25))

def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)    
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv 
        if key == k:
            key_exists = True 
            break
    if key_exists:
        del bucket[i]
        print ('Key {} deleted'.format(key))
    else:
        print ('Key {} not found'.format(key))
 
 
delete(hash_table, 25)
delete(hash_table, 125)
print (hash_table)
