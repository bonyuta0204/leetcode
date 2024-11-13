class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Basic Idea:
            1. walk unvisited cell
            2 - a. if the cell is an island, visit all the cell in the island and mark them as already visited,  then count up island counter
            2 - b. if the cell is an ocean, just mark them visited
            3. back to 1,  keep searching next island
        """

        # we skip validation the here for simplicity
        rows = len(grid)
        columns = len(grid[0])

        unvisited = set()
        island_count = 0

        # build unvisited cell set
        for x in range(rows):
            for y in range(columns):
                unvisited.add((x, y))

        while size(unvisited) > 0:
            current = unvisited.pop()

            if grid[current[0]][current[1]] == "0":
                continue
            else:
                visitIsland(current[0], current[1])
                island_count += 1

        # visit the whole island from single starting point and mark all land as visited
        def visitIsland(x, y):
            adjecent = [(x - 1, y  ), (x, y -1), (x + 1, y) , (x, y + 1)]
            
            for point in adjecent:
                if point is inside grid:
                    return

                if point not in unvisited: 
                    return
                unvisited.del(point)
                elif grid[point[0]][point[1]] == "0":
                    return
                else: 
                    visitIsland(point[0], point[1])









