#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        return sorted(list(map(lambda x: pow(x, 2), nums)))
        '''
        # Use two pointers
        # Find the largest value
        res = []
        left, right = 0, len(nums) - 1 
        while left <= right:
            if nums[left] * nums[left] > nums[right]*nums[right]:
                res.append(nums[left] * nums[left])
                left += 1
            else:
                res.append(nums[right] * nums[right])
                right -= 1

        return res[::-1]






        
# @lc code=end

