#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Pivot index is where the sum of all the numbers to the left
        # is equal to the right
        # My guess is two pointer
        # l, r = 0, len(nums) - 1
        # lsum, rsum = 0, 0
        # while l < r:
            # # I need to pick a sum
            # lsum += nums[l]
            # rsum += nums[r]
            # l += 1
            # if lsum == rsum:
                # return l
            # else:
                # r -= 1
        # return -1

        total = sum(nums)
        lsum = 0
        for i in range(len(nums)):
            rsum = total - nums[i] - lsum
            if lsum == rsum:
                return i
            lsum += nums[i]
        return -1





        
# @lc code=end

