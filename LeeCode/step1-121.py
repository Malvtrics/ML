#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        max_profit = 0
        for i in (range(l)):
            curr_price = prices[i]
            for j in (range(i+1,l)):
                profit = prices[j] - curr_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
        
#思路
#不用判断所有的j，只要找出最小的就可以

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
      l = len(prices)
      max_profit = 0
      min_price = 2147483647 #https://www.youtube.com/watch?v=23cKyM-iFqk 32位计算机能表示的最大数值
      for i in (range(l)):
          curr_price = prices[i]
          if curr_price < min_price:
              min_price = curr_price
          if prices[i] - min_price > max_profit:
              max_profit = prices[i] - min_price
      return max_profit
