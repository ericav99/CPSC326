{-|
    Author: Maxwell Sherman
    Course: CPSC 326, Spring 2019
    Assignment: 10
    Description:
        Haskell implementation of linked list and related functions
-}

-- Define linked list type
data List a = Node a (List a)
            | Nil
            deriving (Show, Eq)

-- Helper function
-- Functions like take but on linked list
llTake :: Int -> List a -> List a
llTake _ Nil = Nil
llTake 0 _ = Nil
llTake n (Node x next)
    | n < 0 = Nil
    | n > (listLen (Node x next)) = (Node x next)
    | n == 0 = (Node x Nil)
    | otherwise = Node x (llTake (n-1) next)

-- Helper function
-- Functions like drop but on linked list
llDrop :: Int -> List a -> List a
llDrop _ Nil = Nil
llDrop 0 node = node
llDrop n (Node x next)
    | n < 0 = (Node x next)
    | n > (listLen (Node x next)) = Nil
    | n == 0 = next
    | otherwise = llDrop (n-1) next

-- Helper function
-- Returns the length of a linked list
listLen :: List a -> Int
listLen Nil = 0
listLen (Node _ next) = 1 + (listLen next)

-- Inserts an item into the end of a linked list
insert :: a -> List a -> List a
insert item Nil = Node item Nil
insert item (Node x next) = Node x (insert item next)

-- Removes the first item matching the target from a linked list
delete :: (Eq a) => a -> List a -> List a
delete _ Nil = Nil
delete t (Node x next)
    | t == x = next
    | otherwise = Node x (delete t next)

-- Returns whether or not a target item exists in a linked list
memberOf :: (Eq a) => a -> List a -> Bool
memberOf _ Nil = False
memberOf t (Node x next)
    | t == x = True
    | otherwise = memberOf t next

-- Returns the element at the given index
-- Creates an error if the index is invalid
elementAt :: Int -> List a -> a
elementAt _ Nil = error "Index out of bounds"
elementAt idx (Node x next)
    | idx < 0 = error "Index out of bounds"
    | idx >= listLen (Node x next) = error "Index out of bounds"
    | idx == 0 = x
    | otherwise = elementAt (idx-1) next

-- Inserts a given item at a given index
-- The item at the specified index is pushed to the right
insertAt :: Int -> a -> List a -> List a
insertAt _ _ Nil = error "Index out of bounds"
insertAt idx item (Node x next)
    | idx < 0 = error "Index out of bounds"
    | idx >= listLen (Node x next) = error "Index out of bounds"
    | idx == 0 = Node item (Node x next)
    | otherwise = Node x (insertAt (idx-1) item next)

-- Deletes the item at the given index
deleteAt :: Int -> List a -> List a
deleteAt _ Nil = error "Index out of bounds"
deleteAt idx (Node x next)
    | idx < 0 = error "Index out of bounds"
    | idx >= listLen(Node x next) = error "Index out of bounds"
    | idx == 0 = next
    | otherwise = Node x (deleteAt (idx-1) next)

-- Concatenates two linked lists of matching type
concatenate :: List a -> List a -> List a
concatenate Nil node = node
concatenate node Nil = node
concatenate (Node x next) node2 = Node x (concatenate next node2)


-- let list1 = Node 8 (Node 6 (Node 7 (Node 5 (Node 3 (Node 0 (Node 9 Nil)))))) is a good test
-- Performs merge sort on a linked list
sortList :: (Ord a) => List a -> List a
sortList Nil = Nil
sortList (Node x Nil) = Node x Nil
sortList (Node x next) =
    let halfway = listLen (Node x next) `div` 2
        merge Nil node = node
        merge node Nil = node
        merge (Node x1 next1) (Node x2 next2)
            | x1 >= x2 = insertAt 0 x2 (merge (Node x1 next1) next2)
            | otherwise = insertAt 0 x1 (merge next1 (Node x2 next2))
    in merge (sortList (llTake halfway (Node x next))) (sortList (llDrop halfway (Node x next)))

-- Functions like map but on linked list
mapList :: (a -> b) -> List a -> List b
mapList _ Nil = Nil
mapList fun (Node x next) = Node (fun x) (mapList fun next)

-- Functions like zipwith but on linked list
zipWithList :: (a -> b -> c) -> List a -> List b -> List c
zipWithList _ Nil _ = Nil
zipWithList _ _ Nil = Nil
zipWithList fun (Node x1 next1) (Node x2 next2) = Node (fun x1 x2) (zipWithList fun next1 next2)
