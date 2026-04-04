class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        mp = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def dfs(i, path):
            if i == len(digits):
                res.append(path)
                return
            
            for c in mp[digits[i]]:
                new_string = path + c
                dfs(i + 1, new_string)
        
        dfs(0, "")

        return res

