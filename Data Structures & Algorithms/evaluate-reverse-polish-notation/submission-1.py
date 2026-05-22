import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ['+', '-', '*', '/']

        for token in tokens:
            if token in operator :
                op2 = stack.pop()
                op1 = stack.pop()
                result = 0
                if token == '+':
                    result = op1 + op2 
                elif token == '-':
                    result = op1 - op2
                elif token == '*':
                    result = op1 * op2
                else:
                    result = op1 / op2
                    if result < 0:
                        result = math.ceil(result)
                    else:
                        result = math.floor(result)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]