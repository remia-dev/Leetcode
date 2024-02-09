#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # How is this a binary search problem?
        # My guess is it should be in between? two non-perfect squares
        # This does not work
        # 1, 4, 9, 16, 25, 36, 49, 56, 64

        '''
        if num < 0:
            return False
        left, right = 0, 1
        while left < num:
            left += right
            right += 2
        return left == num
        '''
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False















        
# @lc code=end

