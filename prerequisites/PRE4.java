/*
PRE4
Send Feedback
There are ‘n’ number of villages. You are given an array of size ‘n’ representing the population of each village. Every year, there is a cricket competition between two teams and villagers who come to see the match. Villagers from ith village and (n-i)-1th village (0 <= i < n/2) are combined and then formed groups of 10 people each. For e.g. villagers from villages 0 and n-1, 1 and n-2, 2 and n-3 are combined. The number of villages is always even. So, clearly there will be n/2 combinations from all the villages. You have to tell how many groups will be formed in each combination and how many villagers will be left without the complete group of 10 peoples.
*/
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int n =sc.nextInt();
        int []a =new int[n];
        int sum=0;
        for(int i=0;i<n;i++)
            a[i]=sc.nextInt();
        for(int i=0;i<n/2;i++)
        {
            sum=a[i]+a[n-1-i];
            System.out.println(sum/10+" "+sum%10);
        }
        
		
	}
}