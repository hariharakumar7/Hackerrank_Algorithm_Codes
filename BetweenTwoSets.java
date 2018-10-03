import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int[] a = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        int[] b = new int[m];
        for(int b_i=0; b_i < m; b_i++){
            b[b_i] = in.nextInt();
        }
        for(int i=0;i<n;i++)
            for(int j=i+1;j<n;j++){
            if(a[i]>a[j]){
                int temp=a[j];
                a[j]=a[i];
                a[i]=temp;
            }
        }
        for(int i=0;i<m;i++)
            for(int j=i+1;j<m;j++){
            if(b[i]>b[j]){
                int temp=b[j];
                b[j]=b[i];
                b[i]=temp;
            }
        }
        int x=a[n-1],y=b[0],count=0;
        for(int i=x;i<=y;i++){
            int flag=0;
            for(int j=0;j<n;j++){
                if(i%a[j]!=0){flag=1;break;}
            }
            for(int j=0;j<m;j++){
                if(b[j]%i!=0){flag=1;break;}
            }
            if(flag==0){count++;}
        }
        System.out.println(count);
    }
}
