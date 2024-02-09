#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # This is kinda hard no?
        # Why do i have the feeling that we'll use two pointers 
        # Maybe?
        # for i in tokens:
        # LIFO - Stack
        '''
        stack = []
        l, r = 0, 1
        while r < len(tokens) - 1:
            if tokens[l].isdigit() and tokens[r] == "+":
                stack.append(int(tokens[l-1]) + int(tokens[l]))
            elif tokens[l].isdigit() and tokens[r] == "/":
                stack.append(int(tokens[l-1]) / int(tokens[l]))
            elif tokens[l].isdigit() and tokens[r] == "*":
                stack.append(int(tokens[l-1]) * int(tokens[l]))
            elif tokens[l].isdigit() and tokens[r] == "-":
                stack.append(int(tokens[l-1]) - int(tokens[l]))
            l = r
            r += 1
        return len(stack)
        '''
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(i))
        return stack[0]

                




# @lc code=end

