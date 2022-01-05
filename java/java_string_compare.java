/**
* author: Chancerel Codjovi (aka codrelphi)
* date: 05-01-2022
* source: https://www.hackerrank.com/challenges/java-string-compare/problem
*/

import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        int taille = s.length();
        
        String[] lexicos = new String[taille];
        
        for (int i=0; i<taille; i++) {
            if (i+k > taille) {
                lexicos[i] = "";
            }
            else {
                lexicos[i] = s.substring(i, i+k);
            }
            
        }
        
        smallest = lexicos[0];
        for (String l : lexicos) {
            if (!l.equals("")) {
                if (smallest.compareTo(l) <= 0) {
                    largest = l;
                }
                else {
                    largest = smallest;
                    smallest = l;
                }
            }
            
        }
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        
        return smallest + "\n" + largest;
    }

