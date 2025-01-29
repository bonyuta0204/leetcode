class Solution:
    def myAtoi(self, s: str) -> int:
        UPPER_LIMIT = 2 ** 31 -1
        LOWER_LIMIT = - (2 ** 31)
        if not s:
            return 0

        index = 0
        sign = 1
        numbers = []

        while  index < len(s) and s[index] == " ":
            index +=1

        if not index < len(s):
            return 0

        if s[index] == "-":
            sign = -1
            index += 1
        elif s[index] == "+":
            sign = 1
            index += 1
        else:
            sign = 1

        while index < len(s) and s[index] == "0":
            index += 1

        while index < len(s) and s[index] in ["0", "1", "2",  "3", "4", "5", "6", "7", "8", "9"]:
            numbers.append(int(s[index]))
            index += 1

        result = 0
        # convert numbers to integer
        for i, value in enumerate(reversed(numbers)):
            result += value * (10 ** i)
        result = result * sign

        if result >= UPPER_LIMIT:
            return UPPER_LIMIT
        elif result <= LOWER_LIMIT:
            return LOWER_LIMIT


        return result




