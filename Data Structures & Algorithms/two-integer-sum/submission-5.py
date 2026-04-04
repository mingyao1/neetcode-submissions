class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index = []

        for i, n in enumerate(nums):
            index.append([n, i])
    

        index.sort()
        l = 0
        r = len(nums) - 1
        
        while not l == r:
            
            total = index[l][0] + index[r][0]

            if total == target:
                return [min(index[l][1], index[r][1]), max(index[l][1], index[r][1])]

            elif total < target:
                l += 1
            elif total > target:
                r -= 1
        return []
        