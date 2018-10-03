import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int arr[]=new int[5];
        int a[]=new int[5];
        String parts[]=br.readLine().split(" ");
        for(int i=0;i<5;i++)
            arr[i]=Integer.parseInt(parts[i]);
        String part[]=br.readLine().split(" ");
        for(int i=0;i<5;i++)
            a[i]=Integer.parseInt(part[i]);
        int total=0;
        for(int i=0;i<5;i++)
            if(arr[i]!=a[i]){
            int temp=Math.abs(arr[i]-a[i]);
            if(temp>5){
                temp=10-temp;
            }
            total+=temp;
        }
        
       System.out.println(total);
    }
}