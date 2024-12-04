module Main where

import qualified Solutions.P104 as P104
import Lib.Types (TreeNode(..))
import Lib.TreeHelper (createTree)

main :: IO ()
main = do
  putStrLn "LeetCode Haskell Solutions"
  putStrLn "========================="
  putStrLn "\nAvailable problems:"
  putStrLn "1. Problem 104 - Maximum Depth of Binary Tree"
  putStrLn "\nRunning examples for all problems:"
  putStrLn "\n----------------------------------------"
  P104.runExample
