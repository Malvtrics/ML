#1160
#学习collections的用法
#https://blog.csdn.net/qwe1257/article/details/83272340 
#使用collections.Counter方法返回统计词频的字典
class Solution(object):
    def countCharacters(self, words, chars):
        res = 0
        t1 = collections.Counter(chars)
        for word in words:
            t2 = collections.Counter(word)
            for c in word:
                if t2[c] > t1[c]:
                    break
            else: #注意这里for else的用法，基础语法还是不够熟练，else就是上面的for循环结束之后走这里，上面的for循环结束，也就是没有发生break
                res += len(word)
        return res
#面试题64 https://leetcode-cn.com/problems/qiu-12n-lcof/
#Python基础and的用法
class Solution(object):
    def sumNums(self, n):
        return n and n + self.sumNums(n-1)
#贝祖定理：若a,b是整数,且gcd(a,b)=d，那么对于任意的整数x,y,ax+by都一定是d的倍数，特别地，一定存在整数x,y，使ax+by=d成立。
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
         return x+y>=z and (z==0 or y and z%math.gcd(x,y)==0)
#判断对称二叉树 101题
