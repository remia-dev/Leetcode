#
# @lc app=leetcode id=1984 lang=python3
#
# [1984] Minimum Difference Between Highest and Lowest of K Scores
#

# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Woudlnt getting the highest and second highest always 
        # result to the lowest?
        # Not necessarily think about the inbetween
        if len(nums) == 1:
            return 0
        # Traversing 
        # R should be the one moving
        '''
        while l < len(nums):
            if r == len(nums)-1:
                l += 1
                r = 1

            diff = nums[l] - nums[r]
            emp.append(diff)
            r += 1
        return min(emp)
        '''
        nums.sort()
        # I dont understand k - 1
        l, r = 0, k - 1
        res = float("inf")
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l, r = l + 1, r + 1
        return res




           

        


# @lc code=end

