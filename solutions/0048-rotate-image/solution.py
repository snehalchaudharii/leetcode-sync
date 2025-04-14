class Solution:
    def rotate(self, A):
        n = len(A)
        # Transpose (swap across diagonal, i < j)
        for i in range(n):
            for j in range(i + 1, n):  # Changed to j > i
                A[i][j], A[j][i] = A[j][i], A[i][j]
        # Reverse each row
        for i in range(n):
            A[i].reverse()
