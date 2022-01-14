/**
* author: Chancerel Codjovi (aka codrelphi)
* date: 14-01-2022
* source: https://www.hackerrank.com/challenges/java-anagrams/problem
*/

import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        boolean result = false;
        if (a.length() != b.length()) return result;
        else {
            for (int i=0; i<a.length(); i++) {
                int countA = 0;
                int countB = 0;
                for (int j=0; j<a.length(); j++) {
                    if (a.charAt(j) == a.charAt(i)) countA++;
                    if (b.charAt(j) == a.charAt(i)) countB++;
                }
                
                if (countA == countB) result = true;
                else result = false;
            }
        }
        return result;
    }

  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
