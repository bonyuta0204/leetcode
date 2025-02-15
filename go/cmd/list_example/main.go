package main

import (
	"fmt"

	"github.com/bonyuta0204/leetcode/go/datastructures"
)

func main() {
	// Create a linked list from a slice
	nums := []int{1, 2, 3, 4, 5}
	list := datastructures.FromSlice(nums)
	fmt.Printf("Created list: %s\n", list)

	// Convert back to slice
	slice := list.ToSlice()
	fmt.Printf("Back to slice: %v\n", slice)

	// Create a single node
	node := datastructures.NewListNode(42)
	fmt.Printf("Single node: %s\n", node)
}
