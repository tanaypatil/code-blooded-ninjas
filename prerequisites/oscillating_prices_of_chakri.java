/*
Oscillating Prices of "Chakri"
Send Feedback
Diwali is here. While everyone here is busy texting "Happy Diwali" wishes to everybody else, NinjaCoder has some other plans and wants to earn some money this season.
Now, the Apex court has allowed the sale of only green crackers this Diwali. Out of all green crackers, "Chakri" is most popular. Because of the irregular supply of "Chakri", the price of "Chakri" is oscillating daily. NinjaCoder saw a business opportunity in this. He/She got a price list for coming N days from an insider in the market union. Prices in the list are for 1 unit of a large packet of "Chakri". Each large packet contains 100 units of Chakri.
Now, due to financial limitations, NinjaCoder can transact only 1 large packet (100 units of "Chakri") in the market. You have to tell maximum profit possible, given that he/she can transact atmost one time.
Note: 1. Transaction refers to the act of buying and selling.
      2. "Chakri" cannot be sold individually. NinjaCoder has to buy/sell the entire packet.
*/
import java.util.Scanner;

public class Main {

	
	public static void main(String[] args) {
		// Write your code here
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        int a[]=new int[n];
        int min, max,temp;
        min =Integer.MAX_VALUE;
        max = Integer.MIN_VALUE;
        for(int i=0;i<n;i++)
        {
            a[i]=sc.nextInt();
        }
        for(int i=0;i<n;i++)
        {
            for(int j=i;j<n;j++)
            {
                temp = a[j]-a[i];
                if(temp>max)
                    max=temp;
                
            }
                
        }
        
        
        System.out.println(max);

	}

} 