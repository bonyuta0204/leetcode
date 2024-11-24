from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        unvisited = set((x, y) for x in range(rows) for y in range(columns))
        island_count = 0

        def visitIsland(x: int, y: int):
            adjacents = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for nx, ny in adjacents:
                # Check if the point is within bounds
                if 0 <= nx < rows and 0 <= ny < columns:
                    if (nx, ny) in unvisited:
                        unvisited.remove((nx, ny))
                        if grid[nx][ny] == "1":
                            visitIsland(nx, ny)  # Recursively visit adjacent land cells

        for x in range(rows):
            for y in range(columns):
                if (x, y) in unvisited:
                    unvisited.remove((x, y))
                    if grid[x][y] == "1":
                        visitIsland(x, y)
                        island_count += 1

        return island_count
