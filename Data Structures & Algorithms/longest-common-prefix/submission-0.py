class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        strs.sort()

        for i in range(len(strs[0])):
            c = strs[0][i]
            flag = True
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    flag = False
                    break
            if not flag:
                break
            else:
                res.append(c)
        
        return "".join(res)