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


