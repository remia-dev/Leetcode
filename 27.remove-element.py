#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        # [3, 2, 2, 3]
        for i in range(len(nums)):
            # [3, 2, 2, 3]
            #  0  1  2  0
            # nums[0] = 3 == 3
            # nums[1] = 2 != 3
            if nums[i] != val:
                # nums[0] = nums[2]
                nums[k] = nums[i]
                k += 1
        return k
        # What i dont understand is why can't i pop it?
   

        
# @lc code=end

