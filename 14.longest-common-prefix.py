#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Getting the corresponding element by index in the array
        '''
         a = ["abc", "def", "ghi"]
         b = list(zip(*a))
         b = [
                ['a', 'd', 'g'],
                ['b', 'e', 'h'],
                ['c', 'f', 'i']
            ]
        '''

        l = list(zip(*strs))
        print(l)
        prefix = ""
        for i in l:
            # I dont get this part
            if len(set(i)) == 1:
                prefix = prefix + i[0]
            else:
                break
        
        return prefix


# @lc code=end

