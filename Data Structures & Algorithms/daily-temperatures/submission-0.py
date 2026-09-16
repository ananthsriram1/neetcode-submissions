class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        stack.append((temperatures[0], 0))

        rv = [0] * len(temperatures)

        for i in range(1, len(temperatures)):

            curr = temperatures[i]
            while len(stack) > 0 and curr > stack[-1][0]:
                
                new_temp, new_index = stack.pop()
                rv[new_index] = i - new_index

            stack.append((temperatures[i], i))

        return rv

        