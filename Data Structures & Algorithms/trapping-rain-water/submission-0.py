"""
[0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 3, 3, 3, 2, 1]
0, 0, 2, 0, 

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        LENGTH = len(height)

        left_arr = [0] * LENGTH
        left_arr[0] = height[0]
        right_arr = [0] * LENGTH
        right_arr[-1] = height[-1]

        for i in range(1, LENGTH):
            left_arr[i] = max(height[i], left_arr[i - 1])

        for i in range(LENGTH - 2, -1, -1):
            right_arr[i] = max(height[i], right_arr[i + 1])

        total = [0] * LENGTH

        for i in range(0, LENGTH):
            total[i] = min(left_arr[i], right_arr[i]) - height[i]

        return sum(total)