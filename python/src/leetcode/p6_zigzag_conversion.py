class Solution:
    def convert(self, s: str, numRows: int) -> str:
        table = [["" for _ in s] for _ in range(numRows)]

        if numRows <= 1:
            return s

        row = 0
        col = 0
        direction = "down"

        for c in s:
            table[row][col] = c

            if direction == "down":
                if row + 1 < numRows:
                    row += 1
                else:
                    direction = "upright"
                    row -= 1
                    col +=1

            elif direction == "upright":
                if row - 1 >= 0:
                    row -= 1
                    col += 1
                else:
                    direction = "down"
                    row += 1

        result = ""
        for row in table:
            for cell in row:
                if cell != "":
                    result += cell

        return result







