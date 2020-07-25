/*
Triplet sum
Send Feedback
Given a random integer array and a number x. Find and print the triplets of elements in the array which sum to x.
While printing a triplet, print the smallest element first.
That is, if a valid triplet is (6, 5, 10) print "5 6 10". There is no constraint that out of 5 triplets which have to be printed on 1st line. You can print triplets in any order, just be careful about the order of elements in a triplet.
Input format :
Line 1 : Integer N (Array Size)
Line 2 : Array elements (separated by space)
Line 3 : Integer x
Output format :
Line 1 : Triplet 1 elements (separated by space)
Line 2 : Triplet 3 elements (separated by space)
Line 3 : and so on
Constraints :
1 <= N <= 1000
1 <= x <= 100
Sample Input:
7
1 2 3 4 5 6 7 
12
Sample Output ;
1 4 7
1 5 6
2 3 7
2 4 6
3 4 5
*/


// arr - input array
// n - size of array

void FindTriplet(int arr[], int n, int x) {
    /* Don't write main().
     * Don't read input, it is passed as function argument.
     * Print output and don't return it.
     * Taking input is handled automatically.
     */
    int i,j,k;
    
    for(int i = 0;i<n;i++){
        for(int j = i;j<n;j++){
            if(arr[i]>arr[j]){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    
    for(i=0;i<n;i++){
        for(j=i;j<n;j++){
            for(k=j;k<n;k++){
                if((arr[i]+arr[j]+arr[k] == x) && i!=j && j!=k && k!=i){
                    printf("%d %d %d\n",arr[i],arr[j],arr[k]);
                }
            }
        }
    }

}
