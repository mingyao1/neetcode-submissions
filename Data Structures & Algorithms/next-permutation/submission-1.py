class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break
        if idx >= 0:
            swap = n
            for i in range(n - 1, idx, -1):
                if nums[i] > nums[idx]:
                    swap = i
                    break
            
            nums[idx], nums[swap] = nums[swap], nums[idx]

        l, r = idx + 1, n - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
