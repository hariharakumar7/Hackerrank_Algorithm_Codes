import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner (System.in);
           int t=sc.nextInt();
        int c=0;
        for(int h=0;h<t;h++)
        {
            
            int a=sc.nextInt();
            int b=sc.nextInt();
            int n=sc.nextInt();
        a=a%1000000007;
        b=b%1000000007;
            if(n==0)
                {
                    System.out.println(a);
                 
            }
        else if(n==1)
            {
            System.out.println(b);
        }
        else if(n>1)
            {
            for(int i=1;i<n;i++)
                {
                c=a+b;
                a=b;
                b=c;
            }
            int temp=c;
            System.out.println(c);
       
        }
    }
}
}