class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, posDiag, negDiag = set(), set(), set()
        
        res = []
        def dfs(r, c, board):
            
            if c in col or (r + c) in posDiag or (r - c) in negDiag or r == n:
                return
            
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            s = ["."] * n
            s[c] = "Q"
            row = "".join(s)
            #print(row)
            board.append(row)
            #print(r)
            if r == n - 1:
                res.append(board.copy())
            
            for i in range(n):
                dfs(r + 1, i, board)
            
            board.pop()
            
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
        
        for c in range(n):
            dfs(0, c, [])
        
        return res