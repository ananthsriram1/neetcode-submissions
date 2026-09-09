class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapping = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in mapping:
                return [mapping[rem], i]

            mapping[nums[i]] = i


        return [0, 1]