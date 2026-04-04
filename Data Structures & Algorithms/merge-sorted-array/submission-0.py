class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = [nums1[i] for i in range(m)]

        p1 = p2 = 0
        idx = 0

        while p1 < m and p2 < n:
            if tmp[p1] <= nums2[p2]:
                nums1[idx] = tmp[p1]
                p1 += 1
            else:
                nums1[idx] = nums2[p2]
                p2 += 1
            idx += 1
        
        if p1 != m:
            while p1 < m:
                nums1[idx] = tmp[p1]
                p1 += 1
                idx += 1
        elif p2 != n:
            while p2 < n:
                nums1[idx] = nums2[p2]
                p2 += 1
                idx += 1
        

        
        