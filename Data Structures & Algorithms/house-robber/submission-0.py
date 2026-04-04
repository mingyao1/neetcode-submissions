class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0

        for n in nums:
            tmp = max(n + r2, r1)
            r2 = r1
            r1 = tmp
        
        return r1


        
