# LeetCode in Go

## Project Structure
```
go/
├── README.md
├── go.mod
├── leetcode/         # LeetCode solutions as a package
│   ├── p20_valid_parentheses.go
│   └── p20_valid_parentheses_test.go
├── datastructures/  # Common data structures used in LeetCode problems
│   ├── list.go      # LinkedList implementation
│   └── list_test.go
└── cmd/             # Example runners for solutions
    ├── p20/
    │   └── main.go
    └── list_example/
        └── main.go
```

## Prerequisites
- Go 1.21 or later
- golangci-lint (for linting)

## Common Data Structures
The `datastructures` package provides implementations of common data structures used in LeetCode problems:

### LinkedList
```go
import "github.com/bonyuta0204/leetcode/go/datastructures"

// Create from slice
list := datastructures.FromSlice([]int{1, 2, 3})

// Create single node
node := datastructures.NewListNode(42)

// Convert to slice
slice := list.ToSlice()

// String representation
fmt.Println(list) // "[1 -> 2 -> 3]"
```

More data structures will be added as needed for solving problems.

## How to Run Solutions
Solutions are organized as a package in `leetcode/`. To run a solution, you can either:

1. Run the tests:
```sh
go test ./...
```

2. Use the example runners in `cmd/`:
```sh
go run cmd/p20/main.go         # Run p20 (Valid Parentheses) example
go run cmd/list_example/main.go # Run LinkedList example
```

3. Import and use in your own code:
```go
import (
    "github.com/bonyuta0204/leetcode/go/leetcode"
    "github.com/bonyuta0204/leetcode/go/datastructures"
)

func main() {
    // Use LeetCode solutions
    result := leetcode.IsValid("()")
    fmt.Println(result)  // true

    // Use data structures
    list := datastructures.FromSlice([]int{1, 2, 3})
    fmt.Println(list)  // [1 -> 2 -> 3]
}
```

## How to Run Lint and Format
We use `golangci-lint` for linting and `gofmt` for formatting (built into Go).

```sh
# Run linter
golangci-lint run

# Format code (will modify files in-place)
go fmt ./...
```

## Adding New Solutions
1. Add your solution in `leetcode/` following the naming convention: `p<number>_<problem_name>.go`
2. Create corresponding test file: `p<number>_<problem_name>_test.go`
3. (Optional) Create an example runner in `cmd/<number>/main.go` if you want to demonstrate usage
4. If you need a new data structure, add it to the `datastructures` package
