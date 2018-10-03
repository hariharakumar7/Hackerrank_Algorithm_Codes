import java.util.*;
class hr{
	static int arr[];
	public static void main(String args[]){
		int t,n,k;	
		Scanner s=new Scanner(System.in);
		t=s.nextInt();
		for(int a=0;a<t;a++)
		{
			n=s.nextInt();
			k=s.nextInt();
			arr=new int[n];
			int count=0;
			for(int i=0;i<n;i++)
			{
				if(n%2==0){
				if(i<n/2)
				arr[2*(i+1)-1]=count;	
				if(i>=n/2)
				arr[2*(n-i-1)]=count;}
				else{
				if(i<n/2)
				arr[2*(i+1)-1]=count;	
				if(i>n/2)
				arr[2*(n-i-1)]=count;	
				if(i==n/2)	
				arr[n-1]=count;
				}
				count++;
			}
            for(int i=0;i<n;i++){
                if(arr[i]==k)
                    System.out.println(i);
            }
			
		}
	}
}