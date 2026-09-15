from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)
        longest = 0
        for num in hashset:

            if num - 1 in hashset:
                continue
            else:
                count = 1
                curr = num
                while curr + 1 in hashset:
                    count += 1
                    curr = curr + 1

                longest = max(count, longest)

        return longest