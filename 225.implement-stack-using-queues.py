#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from collections import deque
class MyStack:
    # This is using stack method
    '''
    def __init__(self):
        # Okay now 
        self.array = []
        # Shouldn't i create a array for the stack
    def push(self, x: int) -> None:
        return self.array.append(x)
    def pop(self) -> int:
        return self.array.pop()
    def top(self) -> int:
        return self.array[-1]
    def empty(self) -> bool:
        return len(self.array) == 0
    '''
    # This is using queue method
    def __init__(self):
        self.queue = deque()

    def push(self, x:int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

