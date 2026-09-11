class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_row(brd, r):
            st = set()
            for i in range(len(brd)):
                index = brd[r][i]
                if index != "." and index in st:
                    return False
                st.add(index)
            return True
        
        def check_col(brd, c):
            st = set()
            for i in range(len(brd)):
                index = brd[i][c]
                if index != "." and index in st:
                    return False
                st.add(index)
            return True

        def check_box(brd, r, c):
            st = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    index = brd[i][j]
                    if index != "." and index in st:
                        return False
                    st.add(index)
            return True
                    

        for i in range(0, 9):
            if not check_row(board, i):
                return False
            if not check_col(board, i):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check_box(board, i , j):
                    return False


        return True
