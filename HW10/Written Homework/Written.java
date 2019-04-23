/*
 * Author: Maxwell Sherman
 * Course: CPSC 326, Spring 2019
 * Assignment: 10
 * Description:
 *   Higher order function examples in Java

import java.util.ArrayList;
import java.util.Arrays;
import java.util.function.Function;

public class Written {
    public static void main(String[] args) {
        Function<Integer, Integer> isEven = x -> x % 2 == 0 ? 1 : 0;
        Function<Integer, Integer> addOne = x -> x + 1;

        ArrayList<Integer> l = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            l.add(i);
        }

        // check if even (1 = true, 0 = false)
        ArrayList<Integer> l2 = myMap(isEven, l);
        for (int item : l2) {
            System.out.print(item + " ");
        }
        System.out.println();

        // empty list
        l2 = myMap(addOne, new ArrayList<Integer>());
        for (int item : l2) {
            System.out.print(item + " ");
        }
        System.out.println();

        // add 1
        l2 = myMap(addOne, l);
        for (int item : l2) {
            System.out.print(item + " ");
        }
        System.out.println();


    }

    public static ArrayList<Integer> myMap(Function<Integer, Integer> func, ArrayList<Integer> lst) {
        ArrayList<Integer> newLst = new ArrayList<>();
        for (int item : lst) {
            newLst.add(func.apply(item));
        }
        return newLst;
    }
}