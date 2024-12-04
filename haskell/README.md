# leetcode-haskell

This repository contains Haskell solutions for LeetCode problems.

## Project Structure

```
.
├── src/
│   ├── Main.hs                        # Main entry point
│   ├── Lib/                           # Common utilities and types
│   │   ├── Types.hs                   # Common data types
│   │   └── TreeHelper.hs             # Helper functions for tree operations
│   └── Solutions/                     # Problem solutions
│       └── P{number}.hs              # Individual problem solutions
├── stack.yaml                         # Stack configuration
└── leetcode-haskell.cabal            # Cabal package configuration
```

## Prerequisites

- [GHC](https://www.haskell.org/ghc/) (Glasgow Haskell Compiler)
- [Stack](https://docs.haskellstack.org/en/stable/) (The Haskell Tool Stack)

## Setup

1. Clone the repository
2. Run `stack setup` to ensure you have the correct GHC version
3. Run `stack build` to compile the project

## Running Solutions

There are several ways to work with the solutions:

### 1. Direct Loading in GHCi (Recommended for Problem Solving)

This is the most straightforward way to work on individual problems:

1. Start GHCi:
   ```bash
   stack ghci
   ```

2. Load the specific problem file:
   ```haskell
   :l src/Solutions/P104.hs
   ```

3. Create and test inputs directly:
   ```haskell
   -- Create a simple tree: Node (Edge 1) (Edge 2) 3
   let a = Edge 1
   let b = Edge 2
   let c = Node a b 3
   
   -- Test the solution
   maxDepth c
   ```


### 2. Compiled Mode

Run all examples through the executable:

1. Build:
   ```bash
   stack build
   ```

2. Run:
   ```bash
   stack exec leetcode-haskell-exe
   ```

## Project Organization

The project is organized into three main parts:

1. **Lib**: Common utilities and types used across multiple problems
   - `Types.hs`: Common data structures (e.g., TreeNode)
   - `TreeHelper.hs`: Helper functions for tree operations

2. **Solutions**: Individual problem solutions
   - Each solution is in its own file named `P{number}.hs`
   - Solutions import common types and helpers from `Lib`
   - Each solution includes:
     - Main problem function(s)
     - Example test cases
     - `runExample` function to demonstrate the solution

3. **Main**: Entry point that runs all examples

## Adding New Solutions

1. Create a new file in `src/Solutions/` with the naming convention `P{number}.hs`
2. Import necessary types and helpers from `Lib`
3. Add the module name to the `other-modules` section in `leetcode-haskell.cabal`
4. Import and add the module's `runExample` to `Main.hs`

## Testing

You can:
1. Load individual problems in GHCi for interactive testing
2. Run the executable to see all examples
