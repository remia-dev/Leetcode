#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l < r:
            mid = (l + r) // 2
            if mid * mid > r:
                r = mid - 1
            elif mid * mid < r:
                l = mid + 1
            else:
                return mid


        
# @lc code=end

