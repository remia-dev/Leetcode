#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # Creating a stack
        # is Stack just a hashMap
        # Consider (), {}, [] as one identity
        hashMap = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i in hashMap:
                # What does stack[-1] mean
                # It means the end of the stack
                if stack and stack[-1] == hashMap[i]:
                    # But wouldn't this pop one only?
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return len(stack) == 0


# @lc code=end

