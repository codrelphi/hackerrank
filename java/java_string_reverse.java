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
        if (taille % 2 == 0) {
            System.out.println("No");
        }
        else {
            int middle = taille/2;
            String fPartA = A.substring(0, middle);
            String sPartA = A.substring(middle+1);
            for (int i=0; i<middle; i++) {
                if (fPartA.charAt(i) == sPartA.charAt(middle-i-1)) {
                    continue;
                }
                else {
                    System.out.println("No");
                    break;
                }
            }
            System.out.println("Yes");         
        }
    }
}



