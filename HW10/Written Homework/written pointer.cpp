/*
 * Author: Maxwell Sherman
 * Course: CPSC 326, Spring 2019
 * Assignment: 10
 * Description:
 *   Higher order function examples in C++
 */

#include <iostream>
#include <vector>

using namespace std;

vector<int> myMap(int (*func)(int), vector<int> lst) {
    int size = lst.size();
    for (int i = 0; i < size; i++) {
        lst[i] = func(lst[i]);
    }
    return lst;
}

int isEven(int x) {
    return x % 2 == 0 ? 1 : 0;
}

int addOne(int x) {
    return x + 1;
}

int main() {
    vector<int> l = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    
    // check if even (1 = true, 0 = false)
    vector<int> l2 = myMap(isEven, l);
    for (auto i : l2) {
        cout << i << ' ';
    }
    cout << endl;
    
    // empty list
    l2 = myMap(isEven, vector<int>());
    for (auto i : l2) {
        cout << i << ' ';
    }
    cout << endl;
    
    // add 1
    l2 = myMap(addOne, l);
    for (auto i : l2) {
        cout << i << ' ';
    }
    cout << endl;
    
    return 0;
}
