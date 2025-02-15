package datastructures

import "fmt"

// ListNode represents a singly-linked list node
type ListNode struct {
	Val  int
	Next *ListNode
}

// NewListNode creates a new ListNode with the given value
func NewListNode(val int) *ListNode {
	return &ListNode{Val: val}
}

// FromSlice creates a linked list from a slice of integers
func FromSlice(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}

	head := &ListNode{Val: nums[0]}
	current := head
	for i := 1; i < len(nums); i++ {
		current.Next = &ListNode{Val: nums[i]}
		current = current.Next
	}
	return head
}

// ToSlice converts a linked list to a slice of integers
func (l *ListNode) ToSlice() []int {
	var result []int
	current := l
	for current != nil {
		result = append(result, current.Val)
		current = current.Next
	}
	return result
}

// String returns a string representation of the linked list
func (l *ListNode) String() string {
	if l == nil {
		return "[]"
	}

	result := "["
	current := l
	for current != nil {
		result += fmt.Sprintf("%d", current.Val)
		if current.Next != nil {
			result += " -> "
		}
		current = current.Next
	}
	result += "]"
	return result
}
