import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = 0
        r = 0

        heap = []
        used_index = set()

        return_maximums = []

        while r < len(nums):
            if (r - l) == k:
                while heap[0][1] in used_index:
                    heapq.heappop_max(heap)

                return_maximums.append(heap[0][0])
                used_index.add(l)

                l += 1

            heapq.heappush_max(heap, (nums[r], r))

            r += 1

        while heap[0][1] in used_index:
            heapq.heappop_max(heap)
        return_maximums.append(heap[0][0])

        return return_maximums





        