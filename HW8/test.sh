#!/bin/bash

echo "Test median3"
ghci hw8.hs > Testing/hw8_result_median3.txt 2>&1 << END
median3 1 2 3
median3 3 1 2
median3 3 1 3
median3 3 1 1
median3 'b' 'a' 'c'
median3 1.5 1.6 1.55
median3 True True False
median3 "ab" "ba" "aa"
:quit
END
echo "Test midpoint"
ghci hw8.hs > Testing/hw8_result_midpoint.txt 2>&1 << END
midpoint (0, 0) (2, 0)
midpoint (-1, -1) (1.0, 3/7)
midpoint (-1, -1) (-1, -1)
midpoint ('a', 'b') ('c', 'd')
:quit
END
echo "Test allButLast"
ghci hw8.hs > Testing/hw8_result_allButLast.txt 2>&1 << END
allButLast [1, 2, 3]
allButLast [1]
allButLast [[("a", "b")], [("c", "d")]]
allButLast []
:quit
END
echo "Test lastElem"
ghci hw8.hs > Testing/hw8_result_lastElem.txt 2>&1 << END
lastElem [1, 2, 3]
lastElem [1]
lastElem [[("a", "b")], [("c", "d")]]
lastElem []
:quit
END
echo "Test elemAt"
ghci hw8.hs > Testing/hw8_result_elemAt.txt 2>&1 << END
elemAt 1 [1, 2, 3]
elemAt 0 [[("a", "b")]]
elemAt 1 [[("a", "b")]]
elemAt (-1) [[("a", "b")]]
elemAt 0 []
elemAt 'a' [1, 2, 3]
:quit
END
echo "Test replaceInList"
ghci hw8.hs > Testing/hw8_result_replaceInList.txt 2>&1 << END
replaceInList [0, 0, 0] 0 4
replaceInList "man" 2 'x'
replaceInList [0, 0, 0] 3 4
replaceInList [0, 0, 0] (-1) 4
replaceInList [0, 0, 0] 0 'a'
replaceInList [0, 0, 0] 'a' 4
:quit
END
echo "Test replaceMax"
ghci hw8.hs > Testing/hw8_result_replaceInMax.txt 2>&1 << END
replaceMax [1, 2, 3]
replaceMax [1, 1, 1]
replaceMax [0]
replaceMax [-5, -5/2, -1.0]
replaceMax [-1, 0, 1]
replaceMax ['A'..'z']
replaceMax []
:quit
END
echo "Test largeToSmallPairs"
ghci hw8.hs > Testing/hw8_result_largeToSmallPairs.txt 2>&1 << END
largeToSmallPairs [5, 4, 2, 3, 1] [5, 2, 3, 1, 4]
largeToSmallPairs [] []
largeToSmallPairs [1, 2, 3] [0]
largeToSmallPairs [1] [0, 1, 2]
largeToSmallPairs [True, True, False, False] [True, False, True, False]
:quit
END
echo "Test containsElem"
ghci hw8.hs > Testing/hw8_result_containsElem.txt 2>&1 << END
containsElem 3 [1, 2, 3, 4, 5]
containsElem 6 [1, 2, 3, 4, 5]
containsElem 'a' [1, 2, 3, 4, 5]
containsElem 'a' "Maxwell"
containsElem 0 []
containsElem True []
:quit
END
echo "Test combine"
ghci hw8.hs > Testing/hw8_result_combine.txt 2>&1 << END
combine 'a' [('b', 10), ('a', 30)] [('c', 10), ('a', 40), ('a', 50)]
combine 5 [(0, 0)] []
combine 5 [('a', 0), ('b', 0)] [('c', 0), ('d', 0)]
combine (True, "hello") [((True, "hello"), 5), ((False, "hello"), 0), ((True, "no"), 4)] [((True, "hello"), 7)]
combine 5 [(5, 0)] [(5, 'a')]
:quit
END
