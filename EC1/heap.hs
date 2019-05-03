{-|
    Author: Maxwell Sherman
    Course: CPSC 326, Spring 2019
    Assignment: Extra Credit 1
    Description:
        Haskell implementation of heap
-}

-- Define heap type
data Heap a = Node a (Heap a) (Heap a)
            | Nil
            deriving (Show, Eq)

-- Helper function
-- Returns whether or not the heap is full
isFull :: Heap a -> Bool
isFull Nil = False
isFull (Node _ Nil Nil) = True
isFull (Node _ l Nil) = False
isFull (Node _ Nil r) = False
isFull (Node _ l r) = isFull l && isFull r && height l == height r

-- Helper function
-- Returns the height of a tree
height :: Heap a -> Int
height Nil = 0
height (Node _ Nil Nil) = 1
height (Node _ l Nil) = 1 + height l
height (Node _ Nil r) = 1 + height r
height (Node _ l r)
        | lHeight > rHeight = 1 + lHeight
        | otherwise = 1 + rHeight
    where lHeight = height l
          rHeight = height r

-- Inserts a value into the heap
insert :: (Ord a) => a -> Heap a -> Heap a
insert a Nil = Node a Nil Nil
insert a (Node x Nil Nil)
    | a >= x = Node x (Node a Nil Nil) Nil
    | otherwise = Node a (Node x Nil Nil) Nil
insert a (Node x l Nil)
    | a >= x = Node x l (Node a Nil Nil)
    | otherwise = Node a l (Node x Nil Nil)
insert a (Node x l r)
    | not (isFull l) || ((isFull r) && (height l) == (height r)) = trickleUp (Node x (insert a l) r) -- then, if (insert a l)'s value is less than x, shift it up
    | otherwise = trickleUp (Node x l (insert a r))

-- Takes a tree where one of the children may be larger than the root
-- And swaps them so the order is correct
-- This is called whenever necessary within insert
trickleUp :: (Ord a) => Heap a -> Heap a
trickleUp (Node x (Node y l1 r1) (Node z l2 r2))
    | y < x = Node y (Node x l1 r1) (Node z l2 r2)
    | z < x = Node z (Node y l1 r1) (Node x l2 r2)
    | otherwise = Node x (Node y l1 r1) (Node z l2 r2)
