from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(index, current, total):

            if total == target:
                result.append(current)
                return

            if index >= len(candidates) or total > target:
                return

            dfs(index, current + [candidates[index]], total + candidates[index])
            dfs(index + 1, current, total)

        dfs(0, [], 0)
        return result
