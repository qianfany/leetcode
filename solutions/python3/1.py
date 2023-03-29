from typing import List


class Solution:
    def twoSum(self, nums, target):
        nums_hash = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_hash:
                return [nums_hash[target - nums[i]], i]
            nums_hash[nums[i]] = i

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty hash map to store the numbers and their indices.
        num_map = {}

        # Iterate through the input list nums using enumerate to get both the index and the number.
        for i, num in enumerate(nums):
            # Calculate the complement of the current number by subtracting it from the target.
            complement = target - num

            # Check if the complement is already in the num_map.
            if complement in num_map:
                # If it is, return the indices of the complement and the current number.
                return [num_map[complement], i]

            # If the complement is not in the num_map, add the current number and its index to the map.
            num_map[num] = i

        # If no solution is found, return an empty list (though it's guaranteed to have a solution in this problem).
        return []


if __name__ == '__main__':
    zhushi = Solution()
    nums = [2, 7, 11, 15]
    print(zhushi.two_sum(nums, 9))
