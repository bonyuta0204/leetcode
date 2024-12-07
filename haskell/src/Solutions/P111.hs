data Tree a = Node a (Tree a) (Tree a) | Empty deriving (Show)

minDepth :: Tree a -> Int
minDepth Empty = 0
minDepth root = bfs [(root, 1)]
  where
    bfs :: [(Tree a, Int)] -> Int
    bfs [] = 0
    bfs ((Empty, depth) : _) = depth - 1
    bfs (((Node _ left right), depth) : xs) = bfs (xs ++ [(left, depth + 1), (right, depth + 1)])
