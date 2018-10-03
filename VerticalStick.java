import java.io.*;
import java.util.*;

public class Solution {

 public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int t= sc.nextInt();
        for(int i=0; i<t;i++){
            int n= sc.nextInt();
            int[] countingArray= new int[1001];
            int[] ar =new int[n];
            for(int j=0; j<n;j++){
                int temp=sc.nextInt();
                ar[j]=temp;
                countingArray[temp]+=1;
            }
            for(int j=1000; j>0; j--){
                countingArray[j-1]=countingArray[j-1]+countingArray[j];
            }
            float exp=0;
            for(int j=0;j<n;j++){
                exp+= (float)(n+1)/(1+countingArray[ar[j]]);
            }
            System.out.printf("%.2f\n" ,exp);
        }
    }
}