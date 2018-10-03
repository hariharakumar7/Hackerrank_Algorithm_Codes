import java.lang.*;
import java.util.*;
class Solution{
	public static void main(String args[]){
		int n,count=0;
		Scanner sc=new Scanner(System.in);
		n=sc.nextInt();
		int arr[]=new int[n];
		for(int i=0;i<n;i++){
			arr[i]=sc.nextInt();
		}
		int dis=2147483647;
		for(int i=0;i<n;i++)
		for(int j=i+1;j<n;j++){
			if(arr[i]==arr[j]){
				if(j-i<dis)dis=j-i;
				count=1;
			}
		}
		if(count==1)
		System.out.println(dis);
		else
		System.out.println("-1");
	}
}