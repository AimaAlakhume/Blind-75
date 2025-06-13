class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        VALIDATE ROWS
        iterate through the board
            create a dictionary
            go through the curr array
                if a number is a digit:
                    if number is in seen:
                        increase value by 1
                    else:
                        store number and set val to 1
            check the dictionary
            if any value is greater than 1
                return false

        TRANSPOSE MATRIX
        transposed_matrix = list(map(list, zip(*board)))

        VALIDATE COLUMNS
        iterate through the board
            create a dictionary
            go through the curr array
                if a number is a digit:
                    if number is in seen:
                        increase value by 1
                    else:
                        store number and set val to 1
            check the dictionary
            if any value is greater than 1
                return false

        VALIDATE 3x3 SUB-BOXES
        initialize a list of 9 sets, sub_boxes = [....]
        iterate through the board with row index 'r' from 0 to len(board)
        iterate through the board with column index 'c' from 0 to len(board)
            if the current cell board[r][c] is a digit:
                find box_index = (r // 3) * 3 + (c // 3)
                if board[r][c] is in sub_boxes[box_index]:
                    Return false
                else:
                    sub_boxes[box_index].add(board[r][c])

        return true
        """
        for row in board:
            seen = dict()
            for num in row:
                if num != '.':
                    if num in seen:
                        seen[num] += 1
                    else:
                        seen[num] = 1
            for key, val in seen.items():
                if val > 1:
                    return False

        transposed_board = list(map(list, zip(*board)))
        for row in transposed_board:
            seen = dict()
            for num in row:
                if num != '.':
                    if num in seen:
                        seen[num] += 1
                    else:
                        seen[num] = 1
            for key, val in seen.items():
                if val > 1:
                    return False

        sub_boxes = [set() for _ in range(9)]
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] != '.':
                    box_index = (r // 3) * 3 + (c // 3)
                    if board[r][c] in sub_boxes[box_index]:
                        return False
                    else:
                        sub_boxes[box_index].add(board[r][c])
        
        return True
