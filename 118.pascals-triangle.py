#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Dont think about it linearly
        # I kinda want to solve this on my own
        tri = []
        # numRows = 4
        for i in range(numRows):
            # row = [1] * (0 + 1) = [1]
            # row = [1] * (1 + 1) = [1, 1]
            # row = [1] * (2 + 1) = [1, 1, 1]
            # row = [1] * (3 + 1) = [1, 1, 1, 1]
            # row = [1] * (4 + 1) = [1, 1, 1, 1, 1]
            row = [1] * (i + 1)
            # print(row)
            for j in range(1, i):
                # Starts at i = 2
                # row[1] = tri[2-1][1-1] + tri[2-1][1]
                # row[1] = tri[1][0] + tri[1][1]
                # row[1] = 1 + 1
                # row[1] = 2
                row[j] = tri[i-1][j-1] + tri[i-1][j]
            print(row)
            tri.append(row)
        return tri

      

        
# @lc code=end

