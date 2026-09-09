from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        counter = Counter(nums)

        for key in counter:
            if counter[key] > 1:
                return True

        return False