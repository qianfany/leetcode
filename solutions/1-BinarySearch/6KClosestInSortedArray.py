class Solution(object):
    def kClosest(self, array, target, k):
        """
        input: int[] array, int target, int k
        return: int[]
        """
        if not array:
            return array
        if k == 0:
            return []

        left = self.largestSmallerEqual(array, target)
        right = left + 1
        result = []

        for _ in range(k):
            if right >= len(array) or (left >= 0 and target - array[left] <= array[right] - target):
                result.append(array[left])
                left -= 1
            else:
                result.append(array[right])
                right += 1

        return result

    def largestSmallerEqual(self, array, target):
        """
        Helper function to find the last element <= target
        Similar to last occurrence binary search
        """
        left, right = 0, len(array) - 1

        while left < right - 1:
            mid = left + (right - left) // 2
            if array[mid] <= target:
                left = mid
            else:
                right = mid

        if array[right] <= target:
            return right
        if array[left] <= target:
            return left
        return -1
