class Solution:

    def binarySearch(self, array, target):
        """
        :type array: List[int]
        :type target: int
        :rtype: int
        LeetCode: 704
        """

        if not array:
            return -1
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

