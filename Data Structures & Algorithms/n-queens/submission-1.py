class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, posDiag, negDiag = set(), set(), set()

        board = [["."] * n for _ in range(n) ]
        
        res = []
        def dfs(r):
            
            if r == n:
                cpy = ["".join(row) for row in board]
                res.append(cpy)
                return

            for c in range(n):
            
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
            
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                dfs(r + 1)
                
                board[r][c] = "."
                
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        
        dfs(0)
        
        return res