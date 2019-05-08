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

-- Helper function
-- Takes a tree where one of the children may be larger than the root
-- And swaps them so the order is correct
-- This is called whenever necessary within insert
trickleUp :: (Ord a) => Heap a -> Heap a
trickleUp (Node x (Node y l1 r1) (Node z l2 r2))
    | y < x = Node y (Node x l1 r1) (Node z l2 r2)
    | z < x = Node z (Node y l1 r1) (Node x l2 r2)
    | otherwise = Node x (Node y l1 r1) (Node z l2 r2)

-- Gets the smallest value from the heap
getMin :: Heap a -> a
getMin Nil = error "Empty Heap"
getMin (Node x _ _) = x

-- Deletes the smallest value from the heap
deleteMin :: (Ord a) => Heap a -> Heap a
deleteMin Nil = Nil
deleteMin (Node x Nil Nil) = Nil
deleteMin (Node x l Nil) = l
deleteMin (Node x Nil r) = r
deleteMin (Node x l r) = trickleDown (deleteLast (Node (lastChild (Node x l r)) l r)) -- This should be fine

-- Helper function
-- Returns the value of the last child
lastChild :: Heap a -> a
lastChild Nil = error "Empty Heap"
lastChild (Node x Nil Nil) = x
lastChild (Node _ l Nil) = lastChild l
lastChild (Node _ _ r) = lastChild r

-- Helper function
-- Removes the last child from the tree
deleteLast :: Heap a -> Heap a
deleteLast Nil = error "Empty Heap"
deleteLast (Node x Nil Nil) = Nil
deleteLast (Node x l Nil) = Node x (deleteLast l) Nil
deleteLast (Node x l r) = Node x l (deleteLast r)

-- Helper function
-- Takes a tree with a non-smallest value at the root
-- And recursively trickles it down until it's ordered properly
trickleDown :: (Ord a) => Heap a -> Heap a
trickleDown (Node x Nil Nil) = Node x Nil Nil
trickleDown (Node x (Node y l r) Nil)
    | y < x = Node y (trickleDown (Node x l r)) Nil
    | otherwise = Node x (Node y l r) Nil
trickleDown (Node x Nil (Node z l r))
    | z < x = Node z Nil (Node x l r)
    | otherwise = Node x Nil (Node z l r)
trickleDown (Node x (Node y l1 r1) (Node z l2 r2))
    | y < x = Node y (trickleDown (Node x l1 r1)) (Node z l2 r2)
    | z < x = Node z (Node y l1 r1) (trickleDown (Node x l2 r2))
    | otherwise = Node x (Node y l1 r1) (Node z l2 r2)

-- Adds each value in a list to the heap
-- foldl won't work here because of the order of insert's parameters
buildHeap :: (Ord a) => [a] -> Heap a -> Heap a
buildHeap [] heap = heap
buildHeap (x:xs) heap = buildHeap xs (insert x heap)

-- Performs heapsort on a list of items
-- Adds them all to a heap, then repeatedly takes the root
heapSort :: (Ord a) => [a] -> [a]
heapSort [] = []
heapSort [x] = [x]
heapSort xs = dumpHeap (buildHeap xs Nil)

-- Helper function
-- Takes a heap, moves the root item to a list recursively
dumpHeap :: (Ord a) => Heap a -> [a]
dumpHeap Nil = []
dumpHeap (Node x Nil Nil) = [x]
dumpHeap heap = (getMin heap) : dumpHeap (deleteMin heap)
