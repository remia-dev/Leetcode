#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # This solution works but it is not binary search
        '''
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            if nums[-1] < target:
                return len(nums)
        '''
        low, high = 0, len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low


   

        
# @lc code=end

