class Solution:
    def kthGrammar(self, n: int,  k: int) -> int:
        """

        We can definne f(n, k) using f(n -1, l).

        if k is odd number
        l = k // 2 + 1

        if f(n-1, l) == 1 => 1
        if f(n-1, l) == 0 => 0
        
        if k is even number
        l = k // 2
        if f(n-1, l) == 1 => 0
        if f(n-1, l) == 0 => 1


        0
        01
        0110
        """

        if n == 1:
            return 0

        if k % 2 == 1:
            return self.kthGrammar(n-1, k // 2 + 1)
        else:
            return (self.kthGrammar(n-1, k // 2)) * -1 + 1

