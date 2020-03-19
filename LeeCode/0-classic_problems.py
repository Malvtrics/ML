#数组、链表、栈、队列、树

#242题 数组
class Solution(object):
    def isAnagram(self, s, t):
        arr = [0] * 26
        for c in s:
            arr[ord(c)-97] += 1
        for c in t:
            arr[ord(c)-97] -= 1
        for i in arr:
            if i != 0:
                return False
        return True
    
#24、25题 链表

#20题 栈
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
        return len(stack) == 1
#739题 栈
#动画理解这个算法
#https://leetcode-cn.com/problems/daily-temperatures/solution/leetcode-tu-jie-739mei-ri-wen-du-by-misterbooo/

#239题 队列、双端队列 用双向链表实现
#初级实现很简单复杂度为nk
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 :
            return []
        ans = []
        for i in range(len(nums)- k + 1):
            tmp = []
            for j in range(k):
                tmp.append(nums[i+j])
            ans.append(max(tmp))
        return ans
#理解python
#https://leetcode-cn.com/problems/sliding-window-maximum/solution/pythonde-shuang-duan-dui-lie-shi-xian-by-monchicke/

#230题 树
