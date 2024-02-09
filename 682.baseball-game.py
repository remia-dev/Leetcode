#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        def is_digit(n):
            try:
                int(n)
                return True
            except ValueError:
                return False


        record = []
        reco2 = []
        for i in range(len(operations)):
            print(reco2)
            if is_digit(operations[i]):
                record.append(operations[i])
                reco2.append(int(operations[i]))
            elif operations[i] == "C":
                record.pop()
                reco2.pop()
                if len(reco2) == 0:
                    return 0
                tmp = record[len(record) - 1]
            elif operations[i] == "D":
                mul = str(eval(tmp ) * 2)
                record.append(mul)
                reco2.append(eval(tmp) * 2)
            elif operations[i] == "+":
                # I need abstraction because i dont understand my code
                # reco2.append(sum(reco2))

                # Get the last element
                lastel = len(reco2) - 1
                last2el = lastel - 1
                add = reco2[lastel] + reco2[last2el]
                # print(reco2[lastel] + reco2[last2el])
                reco2.append(add)
                print(reco2)
        return sum(reco2)
        '''
        record = []
        for i in operations:
            if i == "+":
                summed = record[-2] + record[-1]
                record.append(summed)
            elif i == "D":
                mul = record[-1] * 2
                record.append(mul)
            elif i == "C":
                record.pop()
            else:
                record.append(int(i))

        return sum(record)








        
# @lc code=end

