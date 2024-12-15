class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        We can you dp for solving this problem.
        Path to reach to m, n is combination of path for [m-1, n] and [n, n-1]
        if adjecent path is blocked by a obstacle,  we can just assume that is zero
        """

        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        height = len(obstacleGrid)
        width = len(obstacleGrid[0])

        dp = [ [None for _ in range(width)] for _ in range(height)]

        # we set value to 0 if there is obstacle

        for i in range(height):
            for j in range(width):

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[height - 1][width - 1]


