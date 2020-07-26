/*
Even and Odd Indexes
Send Feedback
Given an array of integers, print two integer values:
First, the sum of all numbers which are even as well as whose index are even.
Second, the sum of all numbers which are odd as well as whose index are odd.
Print the two integers space separated. (Arrays is 0-indexed)
*/
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        int [] a= new int[n];
        int even_sum=0;
        int odd_sum=0;
        for(int i=0;i<n;i++)
        {
            a[i]=sc.nextInt();
            if(i%2==0 && a[i]%2==0)
                even_sum=even_sum+a[i];
            else
            {
                if(i%2!=0 && a[i]%2!=0)
                    odd_sum=odd_sum+a[i];
            }
        }
        System.out.println(even_sum+" "+odd_sum); 
		
	}
}