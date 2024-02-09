#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Dont i just use the zip?
        # This is why zip doesn't work

        strs = [word1, word2]
        mapped = list(zip(*strs))
        conWord = word1[len(word2):]
        conWord2 = word2[len(word1):]


        # print(mapped)
        # The main problem is uneven length
        res = [''.join(i) for i in mapped]
        mal = map(str, res)
        result = ''.join(mal)
        if len(word1) > len(word2):
            return result + conWord
        else:
            return result + conWord2

        # Really need two pointers
        # Alternating
        '''
        l, r = 0, 0
        res = []
        conWord = word1[len(word2):]

        while r < len(word2):
            if l < len(word1):
                res.append(word1[l])
                l += 1
            if r < len(word2):
                res.append(word2[r])
                r += 1
        mal = map(str, res)
        result = ''.join(mal) 
        return result + conWord
        '''






        
# @lc code=end

