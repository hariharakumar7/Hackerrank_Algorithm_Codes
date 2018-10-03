import java.io.*;
import java.util.*;
import java.text.*;
import java.lang.Math;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        double l,q,s1,s2;
        double qi;
        double t,a=0,b,c;
        l=s.nextDouble();
        s1=s.nextDouble();
        s2=s.nextDouble();
        q=s.nextDouble();
        for(double i=0;i<q;i++)
            {
            qi=s.nextDouble();
            c=l-Math.sqrt(qi);
            if(s2>s1)
            a=(s2-s1);
            if(s1>=s2)
                a=s1-s2;
            b=Math.sqrt(2);
            t=c*b/a;
            System.out.println(t);
        }
    }
}