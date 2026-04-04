class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)-1
        
        def binary_search(l, r):
            if l > r:
                return -1
            mid = (l+r) // 2

            print(mid, nums[mid], target)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(l, mid-1)
            else:
                return binary_search(mid+1, r)
        
        
        return binary_search(0, n)