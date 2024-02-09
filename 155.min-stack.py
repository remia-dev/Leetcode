#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    def __init__(self):
        self.array = []
        self.array2 = []
        

    def push(self, val: int) -> None:
        self.array.append(val)
        mini = min(self.array2[-1] if len(self.array2) != 0 else val, val)
        self.array2.append(mini)

        
    def pop(self) -> None:
        self.array.pop()
        self.array2.pop()
        
    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        return self.array2[-1]


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

