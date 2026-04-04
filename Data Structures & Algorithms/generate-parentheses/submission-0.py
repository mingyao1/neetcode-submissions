class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o, c = 0, 0

        res = []
        stack = []

        def backtrack(o, c):
            if o == c == n:
                #print(stack)
                res.append("".join(stack))
                return

            if o < n:
                stack.append("(")
                backtrack(o+1, c)
                stack.pop()
            
            if c < o:
                stack.append(")")
                backtrack(o, c+1)
                stack.pop()
        
        backtrack(o, c)

        return res