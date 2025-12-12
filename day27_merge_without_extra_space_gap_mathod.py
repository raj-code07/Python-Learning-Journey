def mergeArrays(a, b):
    n=len(a)
    m=len(b)
    gap=(n+m+1)//2
    while gap>0:
        i=0
        j=gap
        while j<n+m:
            if j<n and a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
                    
            elif i<n and j>=n and a[i]>b[j-n]:
                a[i],b[j-n]=b[j-n],a[i]
                    
            elif i>=n and b[i-n]>b[j-n]:
                b[i-n],b[j-n]=b[j-n],b[i-n]
                    
            i+=1
            j+=1
                
        if gap == 1:
            break
            
        gap=(gap+1)//2

a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
mergeArrays(a, b)

for ele in a:
    print(ele, end=" ")
print();
for ele in b:
    print(ele, end=" ")