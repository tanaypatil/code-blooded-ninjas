 
n = int(input())
a = list(input().split())
index = 0
odd_sum = 0
even_sum = 0

for number in a:
    if a[index] % 2 ==0 and index%2 ==0:
        even_sum=even_sum+a[index]
    else if a[index] % 2 !=0 and index % 2!=0:
        odd_sum=odd_sum+a[index]

    index=index+1
    
print(even_sum+" "+odd_sum)
