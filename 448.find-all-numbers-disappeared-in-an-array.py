#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # sort = sorted(nums)
        # last = len(sort) 
        # k = []
        # num = 0
        # # for i in sort:
            # # if (i+1) not in sort and i != last:
                # # k.append(i)
            # # if (i+1) not in sort and i != last:
                # # k.append(i+1)
        # while(num < last):
            # num += 1
            # if num not in sort and num != last:
                # k.append(num)

        # return k
        return set(range(1, len(nums)+1)) - set(nums)

            


        
# @lc code=end

