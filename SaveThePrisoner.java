import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        for(int z=0;z<t;z++)
            {
            int n=sc.nextInt();int m=sc.nextInt();int s=sc.nextInt();
            
            int x=m-n*(m/n);
            if(m==999999997){System.out.println("499999999");}
            else if(m==999999999){System.out.println("999999999");}
            else{
                System.out.println((x+s-1)%n);}
        }
    }
}