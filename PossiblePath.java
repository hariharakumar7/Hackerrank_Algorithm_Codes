import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        int t;
        double a,b,x,y,p,q;
        Scanner l=new Scanner(System.in);
        t=l.nextInt();
        for(int i=0;i<t;i++)
            {
        a=l.nextDouble();
        b=l.nextDouble();
        x=l.nextDouble();
        y=l.nextDouble();
        if(a>b)
            {
            p=a;
            q=b;
        }
        else
            {
            p=b;q=a;
        }
            double r=q;
              while(p%q != 0)
        {
            r = p % q;
            p= q;
            q = r;
        }
            if(x>y)
            {
            p=x;
            q=y;
        }
        else
            {
            p=y;q=x;
        }
            double s=q;
              while(p%q != 0)
        {
            s = p % q;
            p= q;
            q = s;
        }
            if(r==s)
                System.out.println("YES");
            else
                System.out.println("NO");
            
        
    }
    }
}