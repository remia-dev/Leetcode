#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # How should I approach this two pointer problem
        # Since it is repeating it doesnt need unique values
        # perform it k times        
        # longest substring
        hashMap = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):

            hashMap[s[r]] = hashMap.get(s[r], 0) + 1

            maxf = max(maxf, hashMap[s[r]])

            while(r - l + 1) - maxf > k:

                hashMap[s[l]] -= 1

                l += 1

            res = max(res, r-l+1)

           
        return res
            


        
            


        # res = windowlen - count[b]
            




# @lc code=end

