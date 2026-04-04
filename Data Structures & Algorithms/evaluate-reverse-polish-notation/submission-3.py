class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}

        for t in tokens:
            if t in ops:
                print(stack)
                y = stack.pop()
                x = stack.pop()
                print(t)
                if t == "+":
                    res = (x + y)
                    stack.append(res)
                elif t == "-":
                    res = (x - y)
                    stack.append(res)
                elif t == "*":
                    res = (x * y)
                    stack.append(res)
                elif t == "/":
                    res = (int(float(x) / y))
                    stack.append(res)
                print(res)
            else:
                stack.append(int(t))
        
        return stack[0]

