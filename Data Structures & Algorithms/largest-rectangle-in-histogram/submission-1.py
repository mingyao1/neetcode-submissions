class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        i = 0

        while i < len(heights):
            start = i
            while stack and heights[i] < stack[-1][1]:
                idx, h = stack.pop()
                res = max(res, (i - idx) * h)
                start = idx
            stack.append((start, heights[i]))
            i += 1

        while stack:
            start, h = stack.pop()
            res = max(res, (i - start) * h)
        
        return res