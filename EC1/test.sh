#!/bin/bash

echo "Test insert"
ghci heap.hs > Testing/heap_insert_result.txt 2>&1 << END
let x = Nil
x
let y = insert 5 x
y
let x = insert 10 y
x
let y = insert 11 x
y
let x = insert 7 y
x
let y = insert 0 x
y
:quit
END
echo "Test getMin"
ghci heap.hs > Testing/heap_getMin_result.txt 2>&1 << END
getMin Nil
getMin (Node 1 Nil Nil)
getMin (Node 1 (Node 3 Nil Nil) (Node 2 Nil Nil))
getMin (Node 4 (Node 8 (Node 10 Nil Nil) (Node 9 Nil Nil)) (Node 5 Nil Nil))
:quit
END
echo "Test deleteMin"
ghci heap.hs > Testing/heap_deleteMin_result.txt 2>&1 << END
deleteMin Nil
deleteMin (Node 1 Nil Nil)
deleteMin (Node 1 (Node 3 Nil Nil) (Node 2 Nil Nil))
deleteMin (Node 2 (Node 4 (Node 10 Nil Nil) (Node 8 Nil Nil)) (Node 5 (Node 9 Nil Nil) Nil))
:quit
END
echo "Test buildHeap"
ghci heap.hs > Testing/heap_buildHeap_result.txt 2>&1 << END
buildHeap [] (Node 1 (Node 3 Nil Nil) (Node 2 Nil Nil))
buildHeap [6, 4, 5] (Node 1 (Node 3 Nil Nil) (Node 2 Nil Nil))
buildHeap [6, 4, 5] Nil
buildHeap [] Nil
:quit
END
echo "Test heapSort"
ghci heap.hs > Testing/heap_heapSort_result.txt 2>&1 << END
heapSort []
heapSort [1]
heapSort [4, 5, 1, 3, 2]
heapSort ['c', 'c', 'a', 'd', 'b']
:quit
END
