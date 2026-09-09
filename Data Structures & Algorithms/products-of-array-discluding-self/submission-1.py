class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        curr = 1
        arr = [1] * len(nums)

        for i in range(len(nums)):
            arr[i] *= curr
            curr *= nums[i]

        curr = 1

        for i in range(len(nums)-1, -1, -1):
            arr[i] *= curr
            curr *= nums[i]

        return arr
        