import dis 
import timeit

def swap1():
    x = 5 
    y = 6 
    x, y = y, x

def swap2():
    x = 5 
    y = 6 
    tmp = x 
    x = y 
    y = tmp 

if __name__ == "__main__":
    print ("================= swap1 =================")
    print (dis.dis(swap1))
    print ("================= swap2 =================")
    print (dis.dis(swap2))
    
 输出结果  
 ================= swap1 =================
  5           0 LOAD_CONST               1 (5)
              3 STORE_FAST               0 (x)

  6           6 LOAD_CONST               2 (6)
              9 STORE_FAST               1 (y)

  7          12 LOAD_FAST                1 (y)
             15 LOAD_FAST                0 (x)
             18 ROT_TWO             
             19 STORE_FAST               0 (x)
             22 STORE_FAST               1 (y)
             25 LOAD_CONST               0 (None)
             28 RETURN_VALUE        
None
================= swap2 =================
 10           0 LOAD_CONST               1 (5)
              3 STORE_FAST               0 (x)

 11           6 LOAD_CONST               2 (6)
              9 STORE_FAST               1 (y)

 12          12 LOAD_FAST                0 (x)
             15 STORE_FAST               2 (tmp)

 13          18 LOAD_FAST                1 (y)
             21 STORE_FAST               0 (x)

 14          24 LOAD_FAST                2 (tmp)
             27 STORE_FAST               1 (y)
             30 LOAD_CONST               0 (None)
             33 RETURN_VALUE        
None


通过字节码可以看到，swap1和swap2最大的区别在于，
swap1中通过ROT_TWO交换栈顶的两个元素实现x和y值的互换，swap2中引入了tmp变量，多了一次LOAD_FAST, STORE_FAST的操作。
执行一个ROT_TWO指令比执行一个LOAD_FAST+STORE_FAST的指令快，这也是为什么swap1比swap2性能更好的原因。
