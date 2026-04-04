class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n + 1] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                continue

            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i] = min(dp[i], dp[i + j] + 1)
                    
        return dp[0]