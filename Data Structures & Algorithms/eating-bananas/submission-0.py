import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        final_k = max(piles)

        while r >= l:

            m = (l + r) // 2
            curr_hours = 0

            for bananas in piles:
                curr_hours += math.ceil(bananas / m)

            
            if curr_hours <= h:
                r = m - 1
                final_k = min(final_k, m)
            else:
                l = m + 1

        return final_k

        