from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        We scan the string one time count each character occurance.
        then,  we scan the string again and see if the character is first uniq character
        """

        counter = defaultdict(int)

        for c in s:
            counter[c] += 1

        for (i, c) in enumerate(s):
            if counter[c] == 1:
                return i

        return -1

