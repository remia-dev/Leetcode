#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        for i, j in enumerate(nums):
            if j == target:
                return i
        return -1
        '''
        # Binary search solution
        l, r = 0, len(nums) - 1
        while l <= r:
            # I think it is because of it started with 0
            mid = l + (r-l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid 
            
        return -1
            


        
# @lc code=end

