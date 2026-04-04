class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        r1, r2 = 0, 0

        for n in nums:
            tmp = max(r2 + n, r1)
            r2 = r1
            r1 = tmp
        
        return r1
