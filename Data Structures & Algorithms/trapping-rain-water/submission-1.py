"""
[0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 3, 3, 3, 2, 1]
0, 0, 2, 0, 

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        LENGTH = len(height)

        max_left = height[0]
        max_right = height[LENGTH - 1]

        l = 0
        r = LENGTH - 1

        total = 0

        while r > l:

            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])
            
            if max_left > max_right:
                total += max_right - height[r]
                r -= 1
            else: 
                total += max_left - height[l]
                l += 1
            
        return total