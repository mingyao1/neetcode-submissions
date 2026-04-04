class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        curMin, curMax = 1, 1

        for n in nums:
            val = n * curMax
            curMax = max(val, n * curMin, n)
            curMin = min(val, n * curMin, n)
            res = max(res, curMax)
        
        return res

        return dp[len(nums)-1]
