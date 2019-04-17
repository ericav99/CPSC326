#!/bin/bash

echo "Test insert"
ghci hw10.hs > Testing/hw10_result_insert.txt 2>&1 << END
let list1 = Node 1 (Node 2 (Node 3 Nil))
let list2 = Nil
let list3 = Node "a" (Node "b" (Node "c" Nil))

insert 4 list1
insert 0 list2
insert "x" list2
insert "xyz" list3
:quit
END
echo "Test delete"
ghci hw10.hs > Testing/hw10_result_delete.txt 2>&1 << END
let list1 = Node 1 (Node 2 (Node 3 Nil))
let list2 = Nil
let list3 = Node "a" (Node "b" (Node "c" Nil))
let list4 = Node 1 (Node 2 (Node 2 (Node 3 Nil)))

delete 2 list1
delete 0 list1
delete 0 list2
delete "a" list2
delete "c" list3
delete 2 list4
:quit
END
echo "Test memberOf"
ghci hw10.hs > Testing/hw10_result_memberOf.txt 2>&1 << END
let list1 = Node 1 (Node 2 (Node 3 Nil))
let list2 = Nil
let list3 = Node "a" (Node "b" (Node "c" Nil))

memberOf 2 list1
memberOf 0 list1
memberOf 0 list2
memberOf "a" list2
memberOf "c" list3
:quit
END
echo "Test elementAt"
ghci hw10.hs > Testing/hw10_result_elementAt.txt 2>&1 << END
let list1 = Node 1 (Node 2 (Node 3 Nil))
let list2 = Nil
let list3 = Node "a" (Node "b" (Node "c" Nil))

elementAt 0 list1
elementAt 2 list3
elementAt (-1) list1
elementAt 3 list1
elementAt 0 list2
:quit
END
echo "Test insertAt"
ghci hw10.hs > Testing/hw10_result_insertAt.txt 2>&1 << END
let list1 = Node 1 (Node 2 (Node 3 Nil))
let list2 = Nil
let list3 = Node "a" (Node "b" (Node "c" Nil))

insertAt 0 5 list1
insertAt 2 "bc" list3
insertAt 3 4 list1
insertAt (-1) 5 list1
insertAt 0 7 list2
insertAt 1 1.5 (insertAt 2 2.5 list1)
:quit
END
echo "Test deleteAt"
ghci hw10.hs > Testing/hw10_result_deleteAt.txt 2>&1 << END
let list1 = Node 1 (Node 2 (Node 3 Nil))
let list2 = Nil
let list3 = Node "a" (Node "b" (Node "c" Nil))

deleteAt 0 list1
deleteAt 2 list3
deleteAt 3 list1
deleteAt 0 list2
deleteAt 1 (deleteAt 2 list3)
:quit
END
echo "Test concatenate"
ghci hw10.hs > Testing/hw10_result_concatenate.txt 2>&1 << END
let list1 = Node 1 (Node 2 (Node 3 Nil))
let list2 = Nil
let list3 = Node "a" (Node "b" (Node "c" Nil))
let list4 = Node 1 (Node 2 (Node 2 (Node 3 Nil)))

concatenate list1 list2
concatenate list2 list3
concatenate list4 list1
:quit
END
echo "Test sortList"
ghci hw10.hs > Testing/hw10_result_sortList.txt 2>&1 << END
let list1 = Node 8 (Node 6 (Node 7 (Node 5 (Node 3 (Node 0 (Node 9 Nil))))))
let list2 = Nil
let list3 = Node "b" (Node "a" Nil)

sortList list1
sortList list2
sortList list3
:quit
END
echo "Test mapList"
ghci hw10.hs > Testing/hw10_result_mapList.txt 2>&1 << END
let list1 = Node 8 (Node 6 (Node 7 (Node 5 (Node 3 (Node 0 (Node 9 Nil))))))
let list2 = Nil
let list3 = Node "b" (Node "a" Nil)

mapList even list1
mapList (\x -> x + 1) list1
mapList even list2
mapList (\x -> x ++ "x") list3
:quit
END
echo "Test zipWithList"
ghci hw10.hs > Testing/hw10_result_zipWithList.txt 2>&1 << END
let list1 = Node 8 (Node 6 (Node 7 (Node 5 (Node 3 (Node 0 (Node 9 Nil))))))
let list2 = Nil
let list3 = Node "b" (Node "a" Nil)
let list4 = Node "x" (Node "y" Nil)
let list5 = Node 1 (Node 2 (Node 3 Nil))

zipWithList (\x y -> x ++ y) list3 list4
zipWithList (\x y -> x + y) list1 list5
zipWithList (\x y -> x + y) list1 list2
:quit
END
