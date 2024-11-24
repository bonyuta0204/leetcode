from typing import List

class Solution:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    using all the original letters exactly once.

    Example 1:
    Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    Explanation:
    - "bat" does not have any anagram in the list.
    - "nat" and "tan" are anagrams as they can be rearranged to form each other.
    - "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

    Example 2:
    Input: strs = [""]
    Output: [[""]]

    Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

    Constraints:
    - 1 <= strs.length <= 10^4
    - 0 <= strs[i].length <= 100
    - strs[i] consists of lowercase English letters.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Strategy:
            1. prepare a function that encode string to a value, in a way that anagrams are encoded same way
            2. group them using the function
        """

        result_hash = {}

        for s in strs:
            encoded = self.encodeString(s)

            if encoded in result_hash:
                result_hash[encoded].append(s)
            else:
                result_hash[encoded] = [s]
        return [v for _, v in result_hash.items()]


    def encodeString(self, s: str) -> str:
        """
        eat => "a1e1t1"
        """
        # カウント用辞書
        counter = {}

        # 各文字のカウント
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        # ソート処理 (キーでソート)
        sorted_counter = sorted(counter.items(), key=lambda c: c[0])

        # "文字+カウント" の形で文字列を作成
        result = ''.join([f"{char}{count}" for char, count in sorted_counter])

        return result



