{-|
    Author: Maxwell Sherman
    Course: CPSC 326, Spring 2019
    Assignment: 9
    Description:
        A collection of simple Haskell functions
        These must not be written with pattern matching or guards
-}

-- Returns the largest value in a list
-- Errors if the list is empty
-- Constraint: Cannot use maximum
myMaximum :: (Ord a) => [a] -> a
myMaximum xs = 
    if null xs
    then error "Empty list"
    else if length xs == 1
    then head xs
    else
        let x = head xs
            y = myMaximum (tail xs)
        in if x >= y
        then x
        else y

-- Returns the list in reverse
-- Constraint: Cannot use reverse
myReverse :: [a] -> [a]
myReverse xs =
    if null xs
    then []
    else
        let n = length xs - 1
        in xs !! n : myReverse (take n xs)

-- Returns the length of a list
-- Constraint: Canont use length
myLength :: [a] -> Int
myLength xs =
    if null xs
    then 0
    else 1 + myLength (tail xs)

-- Returns whether or not a target value is in a list
-- Constraint: Cannot use elem
myElement :: (Eq a) => a -> [a] -> Bool
myElement t xs =
    if null xs                 -- If length 0, target is not in the list
    then False
    else if t == (head xs)     -- Elif target is the head, True
    then True
    else myElement t (tail xs) -- Else, check the rest of the items

-- Returns whether or not all the items in the first list
-- exist within the second list
-- Constraint: Cannot use elems
myElements :: (Eq a) => [a] -> [a] -> Bool
myElements xs ys =
    if null xs
    then True
    else if myElement (head xs) ys
    then myElements (tail xs) ys
    else False

-- Takes a pair of values and a list and returns a new list where
-- each occurrance of the first value (target)
-- is replaced by the second (new)
myReplace :: (Eq a) => (a, a) -> [a] -> [a]
myReplace (t, n) xs =
    if null xs
    then xs
    else if t == head xs
    then n : myReplace (t, n) (tail xs)
    else head xs : myReplace (t, n) (tail xs)

-- Works like myReplace, but takes a list of replacements
-- rather than a single (t, n)
-- Applies the replacements from first to last
myReplaceAll :: (Eq a) => [(a, a)] -> [a] -> [a]
myReplaceAll rs xs =
    if null rs
    then xs
    else myReplaceAll (tail rs) (myReplace (head rs) xs)

-- Returns the sum of all of one element in a list
myElementSum :: (Eq a, Num a) => a -> [a] -> a
myElementSum x xs =
    if null xs || not (myElement x xs)
    then 0
    else if head xs == x
    then x + myElementSum x (tail xs)
    else myElementSum x (tail xs)

-- Removes duplicates from a list
removeDuplicates :: (Eq a) => [a] -> [a]
removeDuplicates xs =
    if null xs
    then []
    else if myElement (head xs) (tail xs)
    then removeDuplicates (tail xs)
    else head xs : removeDuplicates (tail xs)

-- Sorts a list of pairs by the first item in the pair
-- Uses merge sort
mergeSort :: (Ord a) => [(a, b)] -> [(a, b)]
mergeSort xs =
    if null xs
    then []
    else if length xs == 1
    then xs
    else
        let halfway = length xs `div` 2
            merge ms ns =
                if null ms
                then ns
                else if null ns
                then ms
                else if fst (head ms) >= (fst (head ns))
                then head ns : (merge ms (tail ns))
                else head ms : (merge (tail ms) ns)
        in merge (mergeSort (take halfway xs)) (mergeSort (drop halfway xs))
