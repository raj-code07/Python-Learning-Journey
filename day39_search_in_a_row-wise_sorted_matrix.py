def search(arr,x):
    lo,hi=0,len(arr)-1
    while lo<=hi:
        mid=(lo+hi)//2
        
        if x==arr[mid]:
            return True
            
        if x<arr[mid]:
            hi=mid-1
            
        else:
            lo=mid+1
            
    return False
    
    
            
def searchRowMatrix(mat, x):
    n,m=len(mat),len(mat[0])
    for i in range(n):
        if search(mat[i],x):
            return True
                
    return False

mat = [[3, 4, 9],
           [2, 5, 6],
           [9, 25, 27]]
x = 9
if searchRowMatrix(mat, x):
    print("true")
else:
    print("false")