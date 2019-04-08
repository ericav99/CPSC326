#!/bin/bash

echo "Test myMaximum"
ghci hw9a.hs > Testing/hw9_ra_myMaximum.txt 2>&1 << END
myMaximum [7, 1, 9, 12, 10]
myMaximum [("a", 0), ("z", 0), ("n", 0)]
myMaximum [-1, -5]
myMaximum [0]
myMaximum []
:quit
END
ghci hw9b.hs > Testing/hw9_rb_myMaximum.txt 2>&1 << END
myMaximum [7, 1, 9, 12, 10]
myMaximum [("a", 0), ("z", 0), ("n", 0)]
myMaximum [-1, -5]
myMaximum [0]
myMaximum []
:quit
END

echo "Test myReverse"
ghci hw9a.hs > Testing/hw9_ra_myReverse.txt 2>&1 << END
myReverse [5, 2, 4]
myReverse [("a", 0), ("z", 0), ("n", 0)]
myReverse [0]
myReverse []
:quit
END
ghci hw9b.hs > Testing/hw9_rb_myReverse.txt 2>&1 << END
myReverse [5, 2, 4]
myReverse [("a", 0), ("z", 0), ("n", 0)]
myReverse [0]
myReverse []
:quit
END

echo "Test myLength"
ghci hw9a.hs > Testing/hw9_ra_myLength.txt 2>&1 << END
myLength [8, 8, 8, 8]
myLength [("a", 0), ("z", 0), ("n", 0)]
myLength [0]
myLength []
:quit
END
ghci hw9b.hs > Testing/hw9_rb_myLength.txt 2>&1 << END
myLength [8, 8, 8, 8]
myLength [("a", 0), ("z", 0), ("n", 0)]
myLength [0]
myLength []
:quit
END

echo "Test myElement"
ghci hw9a.hs > Testing/hw9_ra_myElement.txt 2>&1 << END
myElement 3 [1, 2, 3, 4]
myElement 5 [1, 2, 3, 4]
myElement 'x' "Maxwell"
myElement 0 "error"
myElement 0 []
myElement 'x' []
:quit
END
ghci hw9b.hs > Testing/hw9_rb_myElement.txt 2>&1 << END
myElement 3 [1, 2, 3, 4]
myElement 5 [1, 2, 3, 4]
myElement 'x' "Maxwell"
myElement 0 "error"
myElement 0 []
myElement 'x' []
:quit
END

echo "Test myElements"
ghci hw9a.hs > Testing/hw9_ra_myElements.txt 2>&1 << END
myElements [2, 3] [1, 2, 3, 4, 5]
myElements [7, 8] [1, 2, 3, 4, 5]
myElements [2, 8] [1, 2, 3, 4, 5]
myElements "zag" "Gonzaga"
myElements [] [1, 2, 3]
myElements [] "Anything"
myElements [1, 2, 3] []
myElements "Anything" []
myElements [] []
myElements [1, 2, 3] "Error"
:quit
END
ghci hw9b.hs > Testing/hw9_rb_myElements.txt 2>&1 << END
myElements [2, 3] [1, 2, 3, 4, 5]
myElements [7, 8] [1, 2, 3, 4, 5]
myElements [2, 8] [1, 2, 3, 4, 5]
myElements "zag" "Gonzaga"
myElements [] [1, 2, 3]
myElements [] "Anything"
myElements [1, 2, 3] []
myElements "Anything" []
myElements [] []
myElements [1, 2, 3] "Error"
:quit
END

echo "Test myReplace"
ghci hw9a.hs > Testing/hw9_ra_myReplace.txt 2>&1 << END
myReplace (2, 8) [1, 2, 3, 2]
myReplace (2, 8) [1, 1, 1]
myReplace (2, 8) []
myReplace (2, 2) [1, 2, 3, 2]
myReplace ('n', 'x') "Man"
myReplace ('o' 0) "Error"
myReplace (0, 1) "Error"
:quit
END
ghci hw9b.hs > Testing/hw9_rb_myReplace.txt 2>&1 << END
myReplace (2, 8) [1, 2, 3, 2]
myReplace (2, 8) [1, 1, 1]
myReplace (2, 8) []
myReplace (2, 2) [1, 2, 3, 2]
myReplace ('n', 'x') "Man"
myReplace ('o' 0) "Error"
myReplace (0, 1) "Error"
:quit
END

echo "Test myReplaceAll"
ghci hw9a.hs > Testing/hw9_ra_myReplaceAll.txt 2>&1 << END
myReplaceAll [('a', 'b'), ('c', 'd')] "abcd"
myReplaceAll [(1, 2), (2, 3)] [1, 2, 3, 4]
myReplaceAll [(1, 2), (2, 3)] []
myReplaceAll [] [1, 2, 3, 4]
:quit
END
ghci hw9b.hs > Testing/hw9_rb_myReplaceAll.txt 2>&1 << END
myReplaceAll [('a', 'b'), ('c', 'd')] "abcd"
myReplaceAll [(1, 2), (2, 3)] [1, 2, 3, 4]
myReplaceAll [(1, 2), (2, 3)] []
myReplaceAll [] [1, 2, 3, 4]
:quit
END

echo "Test myElementSum"
ghci hw9a.hs > Testing/hw9_ra_myElementSum.txt 2>&1 << END
myElementSum 5 [0, 5, 0]
myElementSum 3 [3, 2, 3, 2, 3, 4, 3]
myElementSum 3 []
myElementSum 3 [2, 4, 6, 8]
myElementSum 1.5 [1.5, 1, 2, 1.5, 1.75]
:quit
END
ghci hw9b.hs > Testing/hw9_rb_myElementSum.txt 2>&1 << END
myElementSum 5 [0, 5, 0]
myElementSum 3 [3, 2, 3, 2, 3, 4, 3]
myElementSum 3 []
myElementSum 3 [2, 4, 6, 8]
myElementSum 1.5 [1.5, 1, 2, 1.5, 1.75]
:quit
END

echo "Test removeDuplicates"
ghci hw9a.hs > Testing/hw9_ra_removeDuplicates.txt 2>&1 << END
removeDuplicates ['a', 'b', 'a', 'c', 'b', 'a']
removeDuplicates [10, 11, 13, 11, 12]
removeDuplicates [1, 2, 3]
removeDuplicates []
:quit
END
ghci hw9b.hs > Testing/hw9_rb_removeDuplicates.txt 2>&1 << END
removeDuplicates ['a', 'b', 'a', 'c', 'b', 'a']
removeDuplicates [10, 11, 13, 11, 12]
removeDuplicates [1, 2, 3]
removeDuplicates []
:quit
END

echo "Test mergeSort"
ghci hw9a.hs > Testing/hw9_ra_mergeSort.txt 2>&1 << END
mergeSort [(1, 15), (2, 10), (4, 30)]
mergeSort [("a", 30), ("b", 40), ("c", 20), ("d", 10)]
mergeSort [(1, 0)]
mergeSort []
:quit
END
ghci hw9b.hs > Testing/hw9_rb_mergeSort.txt 2>&1 << END
mergeSort [(1, 15), (2, 10), (4, 30)]
mergeSort [("a", 30), ("b", 40), ("c", 20), ("d", 10)]
mergeSort [(1, 0)]
mergeSort []
:quit
END
