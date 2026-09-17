"""
index has a slope and a y intercept, and we're pretty much trying to figure out when they converge


1 4
4 6
7 8
10 10

4 1 0 7
6 3 1 8
8 5 2 9
10 7 3 10

one solution that comes to mind is a brute force solution, where we add every position to a stack, do a while stack isnt empty, pop off the length of the stack, tracking how many reach the target in each iteration, thats a fleet

"""

from collections import deque
import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        stack = []
        
        for i in range(len(cars)):
            pos, spd = cars[i][0], cars[i][1]

            time = (target - pos) / spd

            if len(stack) > 0 and stack[-1] < time:
                stack.append(time)
            elif len(stack) == 0:
                stack.append(time)

        return len(stack)
        