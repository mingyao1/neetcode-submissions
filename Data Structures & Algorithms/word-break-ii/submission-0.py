class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        cache = {}

        def dfs(i):
            if i == len(s):
                return [""]
            if i in cache:
                return cache[i]
            res = []
            for j in range(i, len(s)):
                if s[i: j + 1] not in words:
                    continue
                strs = dfs(j + 1)
                if not strs:
                    continue
                for st in strs:
                    sentence = s[i: j + 1]
                    if st:
                        sentence += " " + st
                    res.append(sentence)
            cache[i] = res
            return res
        
        return dfs(0)
                        
