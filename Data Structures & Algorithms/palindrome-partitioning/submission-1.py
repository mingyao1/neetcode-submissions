class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                    break
                l += 1
                r -= 1
            return True

        def dfs(i, j, path):
            if j == len(s):
                if i == j:
                    res.append(path.copy())

                return

            dfs(i, j + 1, path)

            if isPalindrome(i, j):
                path.append(s[i: j + 1])
                dfs(j + 1, j + 1, path)
                path.pop()

        dfs(0, 0, [])
        return res

            