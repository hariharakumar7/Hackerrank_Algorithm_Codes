import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = 26;
        int h[] = new int[n];
        for(int h_i=0; h_i < n; h_i++){
            h[h_i] = in.nextInt();
        }
        String str = in.next();
        int max=0;
        for(int i=0;i<str.length();i++){
            char ch=str.charAt(i);
            if(max<h[(int)ch-97]){
                max=h[(int)ch-97];
            }
        }
        System.out.println(max*str.length());
    }
}
