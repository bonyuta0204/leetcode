class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        we use start index and end index and slide one of them at a time.
        if the words are still unique, push end to next index and if not, increment start index

        """

        if len(s) == 0:
            return 0

        start_idx = 0;
        end_idx = 0;

        # we mange which chars are in current substring
        chars = set()

        chars.add(s[0])

        max_chars = 1

        while end_idx < len(s) - 1:
            if s[end_idx + 1] not in chars:
                end_idx += 1
                chars.add(s[end_idx])

                if len(chars) > max_chars:
                    max_chars = len(chars)

            else:
                chars.remove(s[start_idx])
                start_idx += 1
        return max_chars

