import java.io.*;
import java.util.*;
import java.util.concurrent.TimeUnit;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int d1 = in.nextInt();
        int m1 = in.nextInt();
        int y1 = in.nextInt();
        int d2 = in.nextInt();
        int m2 = in.nextInt();
        int y2 = in.nextInt();
        int fine=0;
        /*SimpleDateFormat myFormat = new SimpleDateFormat("dd MM yyyy");
        String inputString1 = d1+" "+m1+" "+y1;
        String inputString2 = d2+" "+m2+" "+y2;
        int fine=0;
        try {
            Date date1 = myFormat.parse(inputString1);
            Date date2 = myFormat.parse(inputString2);
            long diff = date1.getTime() - date2.getTime();
            int days=(int)(TimeUnit.DAYS.convert(diff, TimeUnit.MILLISECONDS));
            if(days<=30 && days>0){
                fine=days*15;
            }
            else if(days<365 &&days>30 ){
                fine=(Math.abs(m1-m2))*500;
            }
            else if(days>365){
                fine=10000;
            }
            System.out.println(fine);
        } 
        catch (ParseException e) {
            e.printStackTrace();
        }*/
        if(y1>y2){
            fine=10000;
        }
        if(m1>m2 && y1==y2){
            fine=(Math.abs(m1-m2))*500;
        }
        if(d1>d2 && m1==m2 && y1==y2){
            fine=(Math.abs(d1-d2))*15;
        }
        System.out.println(fine);
    }
}
