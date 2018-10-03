import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt();
        int arr[]=new int[n];
        for(int i=0;i<n;i++)
            arr[i]=sc.nextInt();
        int charge=sc.nextInt();
        int total=0;
        for(int i=0;i<n;i++)
            if(i!=k)total+=arr[i];
        if(total/2<charge){
            System.out.println(charge-(total/2));
        }
        else{
            System.out.println("Bon Appetit");
        }
    }
}