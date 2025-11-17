arr=[1,2,3,4,5]
def revray(arr):
    n=len(arr)
    for i in range(n//2):
        temp=arr[i]
        arr[i]=arr[n-i-1]
        arr[n-i-1]=temp
    return arr
revray(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")