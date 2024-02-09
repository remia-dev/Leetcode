#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointer
        # Moving from both sides
        newS = ''.join(filter(str.isalnum, s)).strip().replace(' ', '').lower()

        l = 0 
        r = len(newS) - 1
        while l <= r:
            if newS[l] != newS[r]:
                return False
            r -= 1
            l += 1
        return True

# @lc code=end

