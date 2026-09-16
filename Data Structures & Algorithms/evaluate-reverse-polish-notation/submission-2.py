class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        for i in range(0, len(tokens)):
            if tokens[i].lstrip('-').isdigit() and tokens[i] != '-':
                stack.append(int(tokens[i]))

            else:
                second = stack.pop()
                first = stack.pop()
                if tokens[i] == "+":
                    stack.append(first + second)
                elif tokens[i] == "-":
                    stack.append(first - second)
                elif tokens[i] == "*":
                    stack.append(first * second)
                elif tokens[i] == "/":
                    stack.append(int(first / second))

        return stack[-1]