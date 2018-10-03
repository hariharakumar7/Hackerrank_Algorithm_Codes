import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        int len=s.length();
        int sq=(int)Math.sqrt(len);
        int rows=0,col=0;
        if(sq*sq>=len){
            rows=sq;col=sq;
        }
        else if(sq*(sq+1)>=len){
            rows=sq;col=sq+1;
        }
        else{
            rows=sq+1;col=sq+1;
        }
        String arr[][]=new String[rows][col];
        
        int count=0;
        for(int i=0;i<rows;i++)
            for(int j=0;j<col;j++){
            if(count<len){
                arr[i][j]=Character.toString(s.charAt(count));count++;}
            else{
                arr[i][j]="";
            }
        }
        String fin="";
        for(int i=0;i<col;i++){
            for(int j=0;j<rows;j++){
                fin+=arr[j][i];
            }
            fin+=" ";
        }
        System.out.println(fin);
    }
}
