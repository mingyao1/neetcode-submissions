class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2 #A
            j = half - i - 2 #B

            la = A[i] if i >= 0 else float("-infinity")
            ra = A[i + 1] if (i + 1) < len(A) else float("infinity")
            lb = B[j] if j >= 0 else float("-infinity") 
            rb = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if la <= rb and lb <= ra:
                if total % 2:
                    return min(ra, rb)
                
                return (max(la, lb) + min(ra, rb)) / 2
            elif la > rb:
                r = i - 1
            elif lb > ra:
                l = i + 1
        

