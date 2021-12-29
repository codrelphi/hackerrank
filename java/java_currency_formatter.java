/*
	auteur: Chancerel Codjovi (aka codrelphi)
	date: 29.12.2021
	source: https://www.hackerrank.com/challenges/java-currency-formatter/problem
*/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.Scanner;


public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in, "UTF-8");
        double payment = scanner.nextDouble();
        scanner.close();

        // Write your code here.
        String us = NumberFormat.getCurrencyInstance(Locale.US).format(payment);
        String india = NumberFormat.getCurrencyInstance(Locale.US).format(payment);
        String china = NumberFormat.getCurrencyInstance(Locale.CHINESE).format(payment);
        String france = NumberFormat.getCurrencyInstance(Locale.FRENCH).format(payment);
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
