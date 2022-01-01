/**
* author: Chancerel Codjovi (aka codrelphi)
* date: 2020-01-24
* source: https://www.hackerrank.com/challenges/java-loops/problem
* update: 2022-01-01
*/

import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();

        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            int r = a;
            for (int j = 0; j < n; j++) {
                r += Math.pow(2, j) * b;
                System.out.print(r + " ");
            }
            System.out.println();
        }
        in.close();
          
    }
}