#1160
#学习collections的用法
#https://blog.csdn.net/qwe1257/article/details/83272340 
#使用collections.Counter方法返回统计词频的字典
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
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
