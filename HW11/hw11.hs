{-|
    Author: Maxwell Sherman
    Course: CPSC 326, Spring 2019
    Assignment: 11
    Description:
        Further practice with Haskell higher order functions
-}

-- file: main.hs
import System.Environment (getArgs)
import Data.Char (toUpper, isUpper)

-- read input file, apply function to input file, display result
interactWith function inputFile =
  do input <- readFile inputFile
     putStrLn (function input)

-- starting point of the program: call interactWith on "myFunction"
-- where "myFunction" (with type String -> String) must be replaced
-- with the name of the function to call on the input. 
main =
  do args <- getArgs
     case args of
       [input] -> interactWith remWords input
       _ -> putStrLn "error: exactly one argument needed"

-- converts every character in a string to upper case
toUpperCase :: String -> String
toUpperCase xs = map toUpper xs

-- takes a string and filters out the words that don't start
-- with an uppercase letter
capitals :: String -> String
capitals xs = unwords (filter (\x -> isUpper (x !! 0)) (words xs))

-- takes a string with two lines and
-- removes all occurrances of the words on the first line
-- from the second line, and returns the modified second line
remWords :: String -> String
remWords input
        | length (lines input) /= 2 = error "Format incorrect"
        | otherwise = foldl remWord sentence (words targetWords)
    where targetWords = (lines input) !! 0
          sentence = (lines input) !! 1

-- removes every occurrance of a target word from a sentence
remWord :: String -> String -> String
remWord sentence targetWord = unwords(filter (\x -> x /= targetWord) (words sentence))
