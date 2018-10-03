import java.io.*;
import java.util.*;
import java.math.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
         int x=sc.nextInt();
        int count=0;
        int a=2;
        for(int i=1;i<=x;i++)
            {
            count+=a;
            a=(int)(Math.floor(a*3)/2);
        }
        System.out.print(count);
    }
}