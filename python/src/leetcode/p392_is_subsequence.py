class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False

        s_i = 0

        for c in t:
            if c == s[s_i]:
                s_i += 1
                if s_i >= len(s):
                    return True
        return False
