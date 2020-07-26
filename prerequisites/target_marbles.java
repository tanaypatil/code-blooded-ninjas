/*
Target Marbles
Send Feedback
At CodingNinjas, we love to play with marbles. We have many marble games, but the most popular one is “Target Marbles”. Now, our marbles are unique. Each marble has a number on it.
In Target Marbles, the player is given a number in the starting and this number is called target. The player is also given N number of marbles to play with. Now, player has to arrange the marbles in a specific way such that sum of the values of at least one of the continuous subset of the arrangement is equal to given target.
Now, NinjaCoder came to play this game and made an arrangement of marbles. The judges of the game need your help. You have to determine if NinjaCoder has won it or not.
*/
import java.util.Scanner;

public class Main {

	
	public static void main(String[] args) {
		// Write your code here
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        int t = sc.nextInt();
        int a[]= new int[n];
        int start,end,sum,flag;
        
          start=end=sum=flag=0;
        
        for(int i=0;i<n;i++)
        {
            a[i] = sc.nextInt();
            
        }
        while(end<n)
        {
            sum =sum+a[end];
            if(sum==t)
            {
                System.out.println("true");
                printArray(a,start,end);
                flag=1;
                break;
                  
            }
            if(sum>t)
            {
                start=start+1;
                end=start;
                sum=0;
            }
            else
            {
                end++;
            }
        }
        if(flag==0)
            System.out.println("false");
        

	}
    
public static void printArray(int []a, int start, int end)
{
  for(int i = start;i<=end;i++)
      System.out.print(a[i]+" ");
}
    



}