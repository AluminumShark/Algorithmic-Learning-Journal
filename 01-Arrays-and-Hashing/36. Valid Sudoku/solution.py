from typing import List

class Solution:
    """
    Valid Sudoku
    Check if a 9x9 Sudoku board is valid using hash sets for rows, columns, and boxes.
    """
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets for each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == '.':
                    continue
                
                # Calculate box index (0-8)
                # Box layout:
                # 0 1 2
                # 3 4 5
                # 6 7 8
                boxIdx = (r // 3) * 3 + (c // 3)
                
                # Check for duplicates in row, column, or box
                if (val in rows[r]) or (val in cols[c]) or (val in boxs[boxIdx]):
                    return False
                
                # Add value to corresponding sets
                rows[r].add(val)
                cols[c].add(val)
                boxs[boxIdx].add(val)
        
        return True

