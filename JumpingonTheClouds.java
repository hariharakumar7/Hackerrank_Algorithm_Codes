import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int c[] = new int[n];
        for(int c_i=0; c_i < n; c_i++){
            c[c_i] = in.nextInt();
        }
        int count=0;
        int a=0;
        int i=0;
        for(i=0;i<n;i++)
         {
            
            if(i<n-2 &&(c[i+2])==0  ){
                count++;
            
                i+=1;
            }
            
            else if(i<n-1 &&(c[i+1])==0  ){
                count++;
                
            }
            
           }
        if(i==n-2){
            count++;
        }
        
        System.out.print(count++);
    }
}
