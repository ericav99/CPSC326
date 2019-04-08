{-|
    Author: Maxwell Sherman
    Course: CPSC 326, Spring 2019
    Assignment: 9
    Description:
        A collection of simple Haskell functions
        These must be written with pattern matching & guards
-}

-- Returns the largest value in a list
-- Errors if the list is empty
-- Constraint: Cannot use maximum
myMaximum :: (Ord a) => [a] -> a
myMaximum [] = error "Empty list"
myMaximum [a] = a
myMaximum (x:xs)
    | x >= myMaximum xs = x
    | otherwise = myMaximum xs

-- Returns the list in reverse
-- Constraint: Cannot use reverse
myReverse :: [a] -> [a]
myReverse [] = []
myReverse [a] = [a]
myReverse xs = let n = length xs - 1 in xs !! n : myReverse (take n xs)

-- Returns the length of a list
-- Constraint: Canont use length
myLength :: [a] -> Int
myLength [] = 0
myLength (x:xs) = 1 + myLength xs

-- Returns whether or not a target value is in a list
-- Constraint: Cannot use elem
myElement :: (Eq a) => a -> [a] -> Bool
myElement _ [] = False
myElement t (x:xs)
    | t == x = True
    | otherwise = myElement t xs

-- Returns whether or not all the items in the first list
-- exist within the second list
-- Constraint: Cannot use elems
myElements :: (Eq a) => [a] -> [a] -> Bool
myElements [] _ = True
myElements _ [] = False -- This must come after the previous pattern
myElements (x:xs) ys
    | myElement x ys = myElements xs ys
    | otherwise = False

-- Takes a pair of values and a list and returns a new list where
-- each occurrance of the first value (target)
-- is replaced by the second (new)
myReplace :: (Eq a) => (a, a) -> [a] -> [a]
myReplace _ [] = []
myReplace (t, n) (x:xs)
    | t == n = x:xs
    | t == x = n : myReplace (t, n) xs
    | otherwise = x : myReplace (t, n) xs

-- Works like myReplace, but takes a list of replacements
-- rather than a single (t, n)
-- Applies the replacements from first to last
myReplaceAll :: (Eq a) => [(a, a)] -> [a] -> [a]
myReplaceAll _ [] = []
myReplaceAll [] xs = xs
myReplaceAll (r:rs) xs = myReplaceAll rs (myReplace r xs)

-- Returns the sum of all of one element in a list
myElementSum :: (Eq a, Num a) => a -> [a] -> a
myElementSum _ [] = 0
myElementSum t (x:xs)
    | not (myElement t (x:xs)) = 0
    | x == t = t + myElementSum t xs
    | otherwise = myElementSum t xs

-- Removes duplicates from a list
removeDuplicates :: (Eq a) => [a] -> [a]
removeDuplicates [] = []
removeDuplicates (x:xs)
    | myElement x xs = removeDuplicates xs
    | otherwise = x : removeDuplicates xs

-- Sorts a list of pairs by the first item in the pair
-- Uses merge sort
mergeSort :: (Ord a) => [(a, b)] -> [(a, b)]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort xs =
    let halfway = length xs `div` 2
        merge [] ns = ns
        merge ms [] = ms
        merge (m:ms) (n:ns)
            | fst m >= (fst n) = n : (merge (m:ms) ns)
            | otherwise = m : (merge ms (n:ns))
    in merge (mergeSort (take halfway xs)) (mergeSort (drop halfway xs))
