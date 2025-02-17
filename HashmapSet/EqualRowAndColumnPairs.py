from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)
        pairs = 0

        # defaultdict has default value, no need to define it
        rows = defaultdict(int)

        for row in grid:
            rows[tuple(row)] += 1

        for col in range(n):
            # collect all the row values from the col
            column = tuple(grid[r][col] for r in range(n))
            if column in rows:
                pairs += rows[column]

        return pairs
