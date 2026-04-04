class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        r = 0
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
    
        nums1.sort()
        nums2.sort()

        l, r = 0, 0  # Initialize both pointers
        
        while l < len(nums1) and r < len(nums2):
            # 1. Handle Duplicates in nums1
            if l > 0 and nums1[l] == nums1[l-1]:
                l += 1
                continue
                
            # 2. Compare elements
            if nums1[l] == nums2[r]:
                res.append(nums1[l])
                l += 1
                r += 1
            elif nums1[l] < nums2[r]:
                l += 1  # nums1 element is too small, move it up
            else:
                r += 1  # nums2 element is too small, move it up
                
        return res