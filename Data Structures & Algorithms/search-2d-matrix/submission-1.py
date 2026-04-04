class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1
        topRight = matrix[row][col]

        while row < len(matrix) and col >= 0:
            if target == topRight:
                return True
            elif target > topRight:
                row += 1
            elif target < topRight:
                col -= 1
            if col < 0 or row == len(matrix): 
                break
            topRight = matrix[row][col]

        return False