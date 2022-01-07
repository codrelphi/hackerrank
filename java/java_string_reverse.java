/**
* author: Chancerel Codjovi (aka codrelphi)
* date: 07.01.2022
* source: https://www.hackerrank.com/challenges/java-string-reverse/problem
*/

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        
        int taille = A.length();
        int middle = taille/2;
        String firstPartA = A.substring(0, middle);
        String secondPartA = A.substring(middle + 1);
        String temp = "";
        for (int i=0; i<=middle; i++) {
            temp = temp + Character.toString(secondPartA.charAt(i));
        }
        if(firstPartA.equals(temp)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}



