class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if target < matrix[0][0] or target > matrix[len(matrix) - 1][len(matrix[0]) - 1]:
            return False

        t = 0
        b = len(matrix) - 1
        row = -1

        while b >= t:

            m = (t + b) // 2

            if m == len(matrix) - 1:
                if target >= matrix[m][0]:
                    row = m
                    break

            else:
                if target >= matrix[m][0] and target < matrix[m + 1][0]:
                    row = m
                    break
                
                elif target < matrix[m][0]:
                    b = m - 1

                elif target > matrix[m][len(matrix[0]) - 1]:
                    t = m + 1
                
                else:
                    row = m
                    break

        l = 0
        r = len(matrix[row]) - 1

        while r >= l:
            m = (l + r) // 2

            if matrix[row][m] == target:
                return True

            elif matrix[row][m] > target:
                r = m - 1

            elif matrix[row][m] < target:
                l = m + 1

        return False