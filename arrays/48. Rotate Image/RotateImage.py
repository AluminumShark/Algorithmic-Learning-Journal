from typing import List

class Solution:
    """
    Rotate Image (90 degrees clockwise) in-place.
    Idea:
      1) Transpose the matrix (swap across the main diagonal).
      2) Reverse each row.
    This is equivalent to a 90-degree clockwise rotation without extra matrices.
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose (matrix[i][j] <-> matrix[j][i] for j >= i)
        # Only swap for j >= i to avoid double-swapping back
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row (mirror horizontally)
        # This turns the transposed matrix into the 90° clockwise rotated matrix
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
