class Solution:

    def twoSum(self, nums, target):
        nums_hashMap = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_hashMap:
                return [nums_hashMap[target - nums[i]], i]
            nums_hashMap[nums[i]] = i
        raise ValueError("No Two Sum Solution exists")
