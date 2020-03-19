#242题
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
