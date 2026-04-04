class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, remain):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(remain)):
                n = remain.pop(i)
                cur.append(n)
                dfs(cur, remain)
                cur.pop()
                remain.insert(i, n)
        
        dfs([], nums[:])
        return res