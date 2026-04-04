class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            next_row = [0] * (amount + 1)
            next_row[0] = 1

            for a in range(1, amount + 1):
                next_row[a] = dp[a]
                if (a - coins[i]) >= 0:
                    next_row[a] += next_row[a - coins[i]]
            
            dp = next_row
        
        return dp[amount]