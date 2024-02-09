#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        b = sorted(s)
        c = sorted(t)
        return b == c
    
    # Okay now try the hashmap solution
    # d, c = {}, {}
    # Essentially we will count the number of key-value pairs 
    # for i in range(len(s)):
    #     d[s[i]] = d.get(s[i], 0) + 1
    #     c[s[i]] = c.get(s[i], 0) + 1
    
    # return d == c





        
# @lc code=end

