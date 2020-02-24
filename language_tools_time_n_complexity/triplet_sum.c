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
