#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Staircase problem
        # How is this binary search
        l, r = 1, n
        res = 0
        while l <= r:
            mid = (l + r) // 2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res






        
# @lc code=end

