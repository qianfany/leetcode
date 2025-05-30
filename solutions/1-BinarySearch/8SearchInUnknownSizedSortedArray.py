# Definition for a unknown sized dictionary.
class Dictionary(object):
    def get(self, index):
        pass


class Solution(object):
    def search(self, dic, target):
        """
        input: Dictionary dic, int target
        return: int
        """
        if dic is None:
            return -1

        left, right = 0, 1

        while dict.get(right) is not None:
            right *= 2

        while left <= right:
            mid = left + (right - left) // 2
            val = dic.get(mid)

            if val is None:
                right = mid - 1
            elif val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

