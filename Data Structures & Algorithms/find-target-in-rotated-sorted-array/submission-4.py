class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            if target == nums[m]:
                return m
            elif target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            
            if nums[m] < nums[r]:
                if target < nums[r] and target > nums[m]:
                    l = m + 1

                else:
                    r = m - 1

            elif nums[m] > nums[r]:

                if target > nums[l] and target < nums[m]:
                    r = m - 1

                else:
                    l = m + 1

            else:
                return -1

        return -1    
        