import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int q=Integer.parseInt(br.readLine());
        for(int z=0;z<q;z++){
        String part[]=br.readLine().split("");
        String parts[]=br.readLine().split("");
            ArrayList list=new ArrayList();
            for(int i=0;i<part.length;i++)
                list.add(part[i]);
            ArrayList list1=new ArrayList();
            for(int i=0;i<parts.length;i++)
                list1.add(parts[i]);
            int count=0;int flag=0;
            int size=list.size();
        if(part.length>=parts.length){
            for(int i=0;i<list1.size();i++){

                if(list.contains(list1.get(i))){
                    
                    list.remove(list1.get(i));
 
                    count++;
                }
                else if(list.contains(String.valueOf(list1.get(i)).toLowerCase())){
                    list.remove(list1.get(i));
 
                    count++;
                }
                
                
            }
            
            if(count==parts.length){
                flag=1;
            }
            
              
        }
            
            
        if(flag==1){
            System.out.println("YES");
        }
            else{
                System.out.println("NO");
            }
        }
        
    }
}