package main

import (
	"fmt"

	"github.com/bonyuta0204/leetcode/go/leetcode"
)

func main() {
	// Example usage
	testCases := []string{"()", "()[]{}", "(]", "([)]", "{[]}"}
	for _, tc := range testCases {
		fmt.Printf("%s -> %v\n", tc, leetcode.IsValid(tc))
	}
}
