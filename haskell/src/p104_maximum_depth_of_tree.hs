data TreeNode = Node TreeNode TreeNode Int | Edge Int deriving (Show)

maxDepth :: TreeNode -> Int
maxDepth x = case x of
  Node left right _ -> max (maxDepth left) (maxDepth right) + 1
  Edge _ -> 1
