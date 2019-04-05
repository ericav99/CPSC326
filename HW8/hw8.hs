{-|
    Author: Maxwell Sherman
    Course: CPSC 326, Spring 2019
    Assignment: 8
    Description:
        A collection of simple Haskell functions
-}

-- Returns the middle of 3 values.
-- If there are not 3 unique values,
-- it returns the value that occurs most.
-- Takes maximum, then returns the maximum of the remaining vlaues
median3 :: (Ord a) => a -> a -> a -> a
median3 x y z =
    let max = maximum [x, y, z]
        in if max == x
        then maximum [y, z]
        else if max == y
        then maximum [x, z]
        else if max == z
        then maximum [x, y]
        else maximum [x, y] -- this will theoretically never run

-- Returns the midpoint of two 2D cartesian coordinates.
midpoint :: (Floating a) => (a, a) -> (a, a) -> (a, a)
midpoint (a, b) (c, d) =
    ((a + c) / 2, (b + d) / 2)

-- Returns the given list with its last item removed.
-- Error if list is length 0.
-- Constraint: Cannot use init
allButLast :: [a] -> [a]
allButLast lst =
    let len = length lst
        in if len == 0
        then error "List has length 0"
        else take (len - 1) lst

-- Returns the last item of a given list.
-- Error if list is length 0.
-- Constraint: Cannot use last
lastElem :: [a] -> a
lastElem lst =
    lst !! (length lst - 1)

-- Returns the item at index idx in list lst.
-- Constraint: Cannot use (!!)
elemAt :: Int -> [a] -> a
elemAt idx lst =
    if (idx >= length lst || idx < 0)
    then error "Index out of bounds"
    else last (take (idx + 1) lst)

-- Replaces the item at idx in lst with replacement.
replaceInList :: [a] -> Int -> a -> [a]
replaceInList lst idx replacement =
    let firstHalf = take idx lst
        secondHalf = drop (idx + 1) lst
        in if (idx >= length lst || idx < 0)
        then error "Index out of bounds"
        else firstHalf ++ (replacement : secondHalf)

-- Replaces every value in a list
-- with the maximum value in the list.
replaceMax :: (Ord a) => [a] -> [a]
replaceMax lst =
    replicate (length lst) (maximum lst)

-- Returns pairwise elements of lst1 and lst2
-- only where the the element in lst1 > the elemnt in lst2.
largeToSmallPairs :: (Ord a) => [a] -> [a] -> [(a, a)]
largeToSmallPairs lst1 lst2 =
    filter (\(x, y) -> x > y) (zip lst1 lst2)

-- Returns True if element is in lst, else False
-- Constraint: Cannot use elem
containsElem :: (Eq a) => a -> [a] -> Bool
containsElem element lst =
    not (null (filter (\x -> x == element) lst))

-- Returns a list of the elements in lst1 and lst2
-- whose first items match the target
combine :: (Eq a) => a -> [(a, b)] -> [(a, b)] -> [(a, b)]
combine target lst1 lst2 =
    let match (x, y) = x == target
    in (filter match lst1) ++ (filter match lst2)
