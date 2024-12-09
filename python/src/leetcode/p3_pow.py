class Solution:
    def myPow(self, x: float,  n:int) -> float:
        """
        myPow(x, n) = x * myPow(x ,  n - 1)
        myPow(x, n) = myPow(x, n+1) / x
        """

        if n == 0:
            return 1
        elif n > 0:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x, n + 1) / x
