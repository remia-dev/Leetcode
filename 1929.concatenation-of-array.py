#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Merging arrays
        nums2 = []
        for i in nums:
            nums2.append(i)
        return nums + nums2
        # Memory Limit Exceeded
        # Because you'll be appending then it extends

        
# @lc code=end

