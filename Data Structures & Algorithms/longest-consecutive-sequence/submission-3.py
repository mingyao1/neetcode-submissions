class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        length = 0
        for n in nums:
            if n-1 not in nums_set:
                curr = 1
                while n+1 in nums_set:
                    curr += 1
                    n = n+1
                length = max(length, curr)

        return length