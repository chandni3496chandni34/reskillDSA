arr=[1,2,4,5]
sum=0
n=int(input("enter the len of arr"))
total=(n*(n+1))//2
for i in range(0,len(arr)):
    sum=sum+arr[i]
missing=total-sum
print(missing)
#missing=total-sum
