import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static int min(int a,int b){
        if(a<b){
            return a;
        }
        else
            return b;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int p = in.nextInt();
        // your code goes here
        int count=0;
        int turnsf=0,turnsb=0;
        if(n%2==0){
            count++;
            for(int i=0;count<p;i++){
                count+=2;turnsf++;
            }
            count=n;
            for(int i=0;count>p;i++){
                count-=2;turnsb++;
            }
            System.out.println(min(turnsf,turnsb));
        }
        else{
            count++;
            for(int i=0;count<p;i++){
                count+=2;turnsf++;
            }
            count=n;
            count--;
            for(int i=0;count>p;i++){
                count-=2;turnsb++;
            }
            System.out.println(min(turnsf,turnsb));
           
            
        }
         
    }
}
