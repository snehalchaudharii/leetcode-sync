class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    # (i, element): Row check (e.g., (0, "5")).
                    # (element, j): Column check (e.g., ("5", 0)).
                    # (i // 3, j // 3, element): Sub-box check (e.g., (0, 0, "5")).
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))

# Time: O(1) since board is 9x9.
# Loop: 81 iterations.
# Tuple creation: O(1) per cell.
# Set conversion: O(81 * 3) ≈ O(243).
# Total: O(243) ≈ O(1).
# Space: O(1).
