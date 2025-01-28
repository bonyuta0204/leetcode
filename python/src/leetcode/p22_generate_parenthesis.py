from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1. ()
        2. ()(), (())
        3. (()(, ()(()), (()((
        """
        results = []

        def dfs(current, left, right):
            if left == n and right == n:
                results.append(current)

            if left < n:
                dfs(current + "(", left+1, right)

            if right < left:
                dfs(current + ")", left, right + 1)

        dfs("", 0, 0)

        return results


