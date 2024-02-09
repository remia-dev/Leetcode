#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # I cannot sort both strings
        i, j = 0, 0
        # In this case they don't move toward each other?
        # This is more of a sliding window no?
        while(i < len(s) and j < len(t)):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)


            
# @lc code=end

