data Tree a = Node a (Tree a) (Tree a) | Empty deriving (Show)

mergeTree :: Num a => Tree a -> Tree a -> Tree a
mergeTree left right = case left of 
  Empty -> right
  Node l_val l_left l_right -> case right of
    Empty -> left
    Node r_val r_left r_right -> Node (l_val + r_val) (mergeTree l_left r_left) (mergeTree l_right r_right)

