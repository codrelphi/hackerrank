/*
	auteur: Chancerel Codjovi (aka codrelphi)
	date: 29.12.2021
	source: https://www.hackerrank.com/challenges/java-substring/problem
*/

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        int start = in.nextInt();
        int end = in.nextInt();
        
        String result = S.substring(start, end);
        System.out.println(result);
    }
}
