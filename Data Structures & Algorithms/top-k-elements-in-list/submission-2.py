import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        heap = []
        curr_elem = nums[0]
        curr_count = 0

        for i in range(len(nums)):
            if nums[i] == curr_elem:
                curr_count += 1
            else:
                heapq.heappush(heap, (curr_count, curr_elem))

                if len(heap) > k:
                    heapq.heappop(heap)
                
                curr_elem = nums[i]
                curr_count = 1

        heapq.heappush(heap, (curr_count, curr_elem))
        if len(heap) > k:
            heapq.heappop(heap)

        rv = []
        for count, key in heap:
            rv.append(key)

        return rv