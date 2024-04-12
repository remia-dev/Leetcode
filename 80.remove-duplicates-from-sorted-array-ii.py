#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        removed = []
        # Count for hashmap?
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
               hashmap[i] = 1 
            if hashmap[i] != 2:
                removed.append(i)

            

        return len(removed)

        
# @lc code=end


