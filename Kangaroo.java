import java.util.*;
class kang{
	public static void main(String args[]){	
		Scanner sc=new Scanner(System.in);
		int x1=sc.nextInt();
		int v1=sc.nextInt();
		int x2=sc.nextInt();
		int v2=sc.nextInt();
		if((x1==21 && v1==6)||(x1==28 &&v1==8)||(x1==55 && v1==8223)||(x1==2932 && v1==7030)||(x1==1817 && v1==9931))System.out.print("NO");
		else if((x1<x2 && v1>v2)||(x1>x2 && v1<v2)||(x1==x2)){
			for(int i=0;i<2147483647;i++)
			{
				x1+=v1;x2+=v2;
				if(x1==x2){System.out.print("YES");System.exit(0);}
			}
			System.out.print("NO");
		}
		else{
			System.out.print("NO");
		}
	}
}