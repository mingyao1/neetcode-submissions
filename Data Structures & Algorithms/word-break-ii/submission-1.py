class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        res = []
        cur = []

        def dfs(i):
            if i == len(s):
                res.append(" ".join(cur))
                return
            
            for j in range(i, len(s)):
                if s[i: j + 1] in words:
                    cur.append(s[i: j + 1])
                    dfs(j + 1)
                    cur.pop()
            
            return
        dfs(0)
        return res
