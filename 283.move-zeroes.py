#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        # Maintain the relative order without making copies
        while l <= r:
            if nums[l] == 0:
                nums.append(nums[l])
                nums.remove(nums[l])
            l += 1



        
# @lc code=end

