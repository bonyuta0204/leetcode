class Solution:
    def uniquePaths(self, m:int, n:int) -> int:
        """
        The robot can take m + n operation. 
        - m times down and n times right

        so the answer will be
        m + n C m
        """



        smaller = min(m - 1, n -1)



        up = 1 # denomi
        down = 1

        for i in range(smaller):
           up = up * (m + n-2 - i)
           down = down * (smaller - i)

        return up // down # guranteed to be an integer

