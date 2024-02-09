#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # One that would return me max profit
        # find the lowest
        # LEFT AND RIGHT POINTER
        # LEFT - buy
        # RIGHT - sell
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            currentProfit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                max_profit = max(max_profit, currentProfit)
            else:
                l = r
            r+=1
        return max_profit
        

        
# @lc code=end
