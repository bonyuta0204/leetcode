package datastructures

import (
	"reflect"
	"testing"
)

func TestFromSlice(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want []int
	}{
		{
			name: "empty slice",
			nums: []int{},
			want: nil,
		},
		{
			name: "single element",
			nums: []int{1},
			want: []int{1},
		},
		{
			name: "multiple elements",
			nums: []int{1, 2, 3, 4, 5},
			want: []int{1, 2, 3, 4, 5},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			list := FromSlice(tt.nums)
			got := list.ToSlice()
			if list == nil && tt.want == nil {
				return
			}
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("FromSlice() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestString(t *testing.T) {
	tests := []struct {
		name string
		list *ListNode
		want string
	}{
		{
			name: "nil list",
			list: nil,
			want: "[]",
		},
		{
			name: "single node",
			list: &ListNode{Val: 1},
			want: "[1]",
		},
		{
			name: "multiple nodes",
			list: FromSlice([]int{1, 2, 3}),
			want: "[1 -> 2 -> 3]",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.list.String(); got != tt.want {
				t.Errorf("String() = %v, want %v", got, tt.want)
			}
		})
	}
}
