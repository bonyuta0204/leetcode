package leetcode

// IsValid determines if the input string has valid parentheses
// LeetCode Problem 20: https://leetcode.com/problems/valid-parentheses/
func IsValid(s string) bool {
	stack := make([]rune, 0)

	pairs := map[rune]rune{
		')': '(',
		'}': '{',
		']': '[',
	}

	for _, char := range s {
		switch char {
		case '(', '{', '[':
			stack = append(stack, char)
		case ')', '}', ']':
			if len(stack) == 0 {
				return false
			}
			if stack[len(stack)-1] != pairs[char] {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) == 0
}
