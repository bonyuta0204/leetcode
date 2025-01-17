class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
       """
       Use bfs to find all the area in an island
       """ 

       if not grid:
           return 0

       row_size = len(grid)
       col_size = len(grid[0])

       max_area = 0

       def get_island_area(position):
            """
            Use DFS to visite all node and return the sum
            """

            adjecent_move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            # currently visiting node
            area = 1

            # mark the cell as visited
            grid[position[0]][position[1]] = 0

            for move in adjecent_move:
                candidate = (position[0] + move[0],  position[1] + move[1])

                if 0 <= candidate[0] < row_size and 0 <= candidate[1] < col_size:
                    if grid[candidate[0]][candidate[1]] == 1:
                        area += get_island_area(candidate)

            return area




       for row_idx in range(row_size):
           for col_idx in range(col_size):
               if grid[row_idx][col_idx] == 0:
                   continue
               else:
                   area = get_island_area((row_idx, col_idx))

                   if area > max_area:
                       max_area = area

       return max_area
