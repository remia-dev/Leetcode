#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use of Hashset
        hashset = {}
        for word in strs:
            # Sort alphabetically 
            temp = ''.join(sorted(word))
            if temp in hashset:
                # Hashset[temp]
                # aet : ['eat', 'tea', 'ate']
                hashset[temp].append(word)
            else:
                # ant : ['tan']
                hashset[temp] = [word]

        return list(hashset.values())




        
# @lc code=end

