#LIS longest increasing sequence 最长上升子序列问题
#300 题目 https://leetcode-cn.com/problems/longest-increasing-subsequence/
#思路：用一个dp数组来保存历史最长子序列长度，这个是有了思路之后自己写出的代码，没有直接参考答案，复杂度O(N*N)
#需要进一步优化为nlogn， 先按照思路解决面试17.08题 https://leetcode-cn.com/problems/circus-tower-lcci/
class Solution(object):
    def lengthOfLIS(self, nums):
        dp = []
        ans = 0
        for i in range(len(nums)):
            dp.append(1)
            maxdp = 0
            for j in range(i):
                if nums[j] < nums[i] and dp[j] > maxdp:
                    maxdp = dp[j]
            dp[i] += maxdp
            if dp[i] > ans:
                ans = dp[i]
        return ans
 #面试17.08题 https://leetcode-cn.com/problems/circus-tower-lcci/
 #没做出来，直接看解法  https://leetcode-cn.com/problems/circus-tower-lcci/solution/python-solutiontan-xin-er-fen-cha-zhao-by-gareth/
 #官方的贪心加二分查找方法
 class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)
