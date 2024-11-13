class Solution: 
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if len(stack) > 0 and self.isPair(stack[-1] , c):
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0


    def isPair(self,open_char, close_char):
        if open_char == "(" and close_char == ")":
            return True
        elif open_char == "{" and close_char == "}":
            return True
        elif open_char == "[" and close_char == "]":
            return True
        else:
            return False
