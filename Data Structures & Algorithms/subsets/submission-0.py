class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        
        res = []
        idx = -1
        
        def dfs(curList, idx):
            if idx == len(nums):
                return
            
            res.append(curList)
            for i in range(len(nums)):
                if i > idx:
                    cpy = curList.copy()
                    cpy.append(nums[i])
                    dfs(cpy, i)
        
        dfs([], idx)

        return res



                
        
