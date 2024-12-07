module Solutions.P104
  ( maxDepth,
    runExample,
  )
where

import Lib.TreeHelper (createTree)
import Lib.Types (TreeNode (..))

-- | Maximum Depth of Binary Tree
-- | Given the root of a binary tree, return its maximum depth.
maxDepth :: TreeNode -> Int
maxDepth x = case x of
  Node left right _ -> max (maxDepth left) (maxDepth right) + 1
  Edge _ -> 1
  Empty -> 0

-- Example test cases
example1 :: TreeNode
example1 = createTree [Just 3, Just 9, Just 20, Nothing, Nothing, Just 15, Just 7]

example2 :: TreeNode
example2 = createTree [Just 1, Nothing, Just 2]

-- Function to run all examples
runExample :: IO ()
runExample = do
  putStrLn "Running examples for Problem 104: Maximum Depth of Binary Tree"
  putStrLn "Example 1:"
  putStrLn $ "Input: " ++ show example1
  putStrLn $ "Output: " ++ show (maxDepth example1)
  putStrLn "\nExample 2:"
  putStrLn $ "Input: " ++ show example2
  putStrLn $ "Output: " ++ show (maxDepth example2)
