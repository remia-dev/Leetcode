#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Maybe use enumerate?
        hashmap = {}
        for (index, value) in enumerate(nums):
            # diff = 9 - 2
            # diff = 7
            diff = target - value
            # Because I am finding a value equal to 7
            if diff in hashmap:
                return [hashmap[diff], index]
            # else put it into hashmap
            # hashmap = {2: 0}
            hashmap[value] = index




        
# @lc code=end

