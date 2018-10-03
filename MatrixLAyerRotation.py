import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int k=sc.nextInt();
        int arr[][]=new int[n+2][m+2];
        for(int i=0;i<n+2;i++){
            if(i==0||i==n+1){
                for(int j=0;j<m+2;j++){
                    arr[i][j]=-1;
                }
            }
            else{
                arr[i][0]=-1;
                arr[i][m+1]=-1;
            }
        }
        
        for(int i=1;i<n+1;i++)
            {
            
            for(int j=1;j<m+1;j++){
                arr[i][j]=sc.nextInt();
            }
            
        }
        ArrayList al,ar;
        ar=new ArrayList();
        for(int i=1;i<=Math.min(((n/2)+(n%2)),((m/2)+(m%2)));i++){
     
            al=new ArrayList();
                for(int j=i;j<m+2-i;j++){
                    if(!al.contains(arr[i][j]))
                    al.add(arr[i][j]);
                    //System.out.print(arr[i][j]);
                    //System.out.print(" ");
                }
                
              
                for(int j=i;j<n+2-i;j++){
                    if(!al.contains(arr[j][m+2-i-1]))
                    al.add(arr[j][m+2-i-1]);
                    //System.out.print();
                    //System.out.print(" ");
                }
                for(int j=m+2-i-1;j>i-1;j--){
                    if(!al.contains(arr[n+2-i-1][j]))
                    al.add(arr[n+2-i-1][j]);
                    //System.out.print(arr[n+2-i-1][j]);
                    //System.out.print(" ");
                }
                for(int j=n+2-i-1;j>i-1;j--){
                    if(!al.contains(arr[j][i]))
                    al.add(arr[j][i]);
                    //System.out.print(arr[j][i]);
                    //System.out.print(" ");
                }
                ar.add(al);
            
          }
        //System.out.println(ar);
        for(int i=0;i<ar.size();i++){
            ArrayList aa=(ArrayList)ar.get(i);
            int l=aa.size();
            ArrayList abc=new ArrayList();
            for(int x=0;x<aa.size();x++)
            abc.add(aa.get((((-k+l)%l)+l)%l));
            System.out.println(abc);
        }
        
    }
}

//time="00"+time[2:]