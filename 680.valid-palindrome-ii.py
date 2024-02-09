#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # There should be 2 of every letter
        # At most there should only be 1 of 1 letter
        # All palindrome are off numbers
        # We dont know if what we need to delete is the right or left pointer
        def isPal(lp, rp):
            while lp < rp:
                if s[lp] == s[rp]:
                    lp += 1
                    rp -= 1
                else:
                    return False
            return True
        
        l,r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1 
                r -= 1
            else:
                return isPal(l, r-1) or isPal(l + 1, r)
        return True
    


        
# @lc code=end

