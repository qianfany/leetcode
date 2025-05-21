class Solution(object):
    def closest(self, array, target):
        """
        input: int[] array, int target
        return: int
        """
        if not array:
            return -1

        left, right = 0, len(array) - 1

        while left < right - 1:
            mid = left + (right - left) // 2
            if array[mid] <= target:
                left = mid
            else:
                right = mid

        if abs(array[right] - target) < abs(array[left] - target):
            return right
        else:
            return left
