
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        We start from (0, 0) and if we find a island, proble all cells in island.
        To find all cells of an island, we can use BFS and mark visited cell to water
        """

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        result = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                else:
                    # find all the area and adds up cell

                    queue = deque([(i, j)])

                    offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                    while queue:
                        next_pos = queue.popleft()

                        if 0 <= next_pos[0] < rows and 0<= next_pos[1] < cols and grid[next_pos[0]][next_pos[1]] == 1:
                            result += 1
                            grid[next_pos[0]][next_pos[1]] = 0

                            for offset in offsets:
                                queue.append((next_pos[0] + offset[0], next_pos[1] + offset[1]))


        return result
