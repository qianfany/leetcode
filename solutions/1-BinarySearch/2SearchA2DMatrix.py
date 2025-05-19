class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        LeetCode: 74
        """
        result = [-1, -1]
        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = matrix[mid // col][mid % col]
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
