class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        l = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            
            while count > k:
                while nums[l] == 1:
                    l += 1
                l += 1
                count -= 1
            
            res = max(res, r - l + 1)
        
        return res 