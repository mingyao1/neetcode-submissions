class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]

        while l < r:
            if max_l < max_r:
                res += max(0, max_l - height[l])
                l += 1
                max_l = max(max_l, height[l])
            else:
                res += max(0, max_r - height[r])
                r -= 1
                max_r = max(max_r, height[r])
        return res