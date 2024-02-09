#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substring without repeating characters
        # Two pointers cannot be used here
        # Unique characters
        # Sets?
        # Maybe two pointers? cant be because it is not an array
        b = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in b:
                b.remove(s[l])
                l += 1
            b.add(s[r])
            # I dont get the result
            res = max(res, r-l + 1)
        return res

            
        

        
# @lc code=end

