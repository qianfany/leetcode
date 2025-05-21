class Solution(object):
    def smallestElementLargerThanTarget(self, array, target):
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
                left = mid + 1
            else:
                right = mid

        if array[left] > target:
            return left
        if array[right] > target:
            return right
        return -1


