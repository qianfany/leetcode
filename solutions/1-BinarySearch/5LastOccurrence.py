class Solution(object):
    def lastOccur(self, array, target):
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

        if array[right] == target:
            return right
        if array[left] == target:
            return left
        return -1
