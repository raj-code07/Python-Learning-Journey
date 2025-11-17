arr=[1,2,3,4,5] 
n=len(arr)
def revray(arr):
   
    temp=[0]*n
    for i in range(n):
        temp[i]=arr[n-i-1]
    for i in range(n):
        arr[i]=temp[i]
    return arr
revray(arr)
for i in range(n):
    print(arr[i], end=" ")
    


    

