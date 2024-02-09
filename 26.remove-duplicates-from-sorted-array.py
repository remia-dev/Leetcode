#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # remove duplictes without creating a new datatype
        # It TLEs in this solution
        '''
        l, r = 0, 1
        while r < len(nums) - 1:
            if nums[l] == nums[r]:
                nums.remove(nums[l])
                l += 1
                r += 1
        '''
        nums[:] = sorted(set(nums))
        return len(nums)
   




# @lc code=end

