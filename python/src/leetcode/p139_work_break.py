from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        solvable = [False for _ in s]

        for i in reversed(range(len(s))):
            if s[i:] in words:
                solvable[i] = True
                continue

            for j in range(i, len(s)):
                if s[i:j] in words and solvable[j] == True:
                    solvable[i] = True
                    break
        return solvable[0]

