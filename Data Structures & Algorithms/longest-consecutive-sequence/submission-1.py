class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        #print(nums)
        length, curr = 1, 1
        prev = nums[0]
        for n in nums[1:]:
            print(prev, n, length)
            if n == prev:
                continue
            if n == prev + 1:
                curr += 1
            else:
                curr = 1
            prev = n
            length = max(length, curr)
        return length