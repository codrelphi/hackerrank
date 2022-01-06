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
        int sLength = s.length();
        sLength = sLength - k + 1;
        
        String[] lexicos = new String[sLength];
        
        for (int i=0; i<sLength; i++) {
            lexicos[i] = s.substring(i, i+k);
        }
        
        smallest = lexicos[0];
        largest = lexicos[0];
        
        for (String l : lexicos) {
            
            // find smallest 
            if (smallest.compareTo(l) > 0) {
                smallest = l;
            }
            
            // find largest
            if (largest.compareTo(l) <= 0) {
                largest = l;
            }
        }
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        
        return smallest + "\n" + largest;
    }

