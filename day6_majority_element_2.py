
arr=[1,2,2,2,2,3,3,3,3]
def findMajority(arr):
    n=len(arr) 
    freq={}
    res=[]
        
    for i in arr:
        freq[i]=freq.get(i,0)+1
    for k,v in freq.items():
        if v>n//3:
            res.append(k)
    if len(res)==2 and res[0]>res[1]:
        res[0],res[1]=res[1],res[0]
    return res

res=findMajority(arr)
for i in res:
    print(i,end=" ")