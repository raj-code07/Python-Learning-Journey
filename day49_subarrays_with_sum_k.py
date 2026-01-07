def cntSubarrays(arr, k):
    prefixSums={}
    res=0
    currSum=0
        
    for i in arr:
        currSum+=i
            
        if currSum == k:
            res+=1
                
        if currSum-k in prefixSums:
            res+=prefixSums[currSum-k]
                
                
        prefixSums[currSum]=prefixSums.get(currSum,0)+1
            
    return res

arr=[32,54,3,4,2,5,6,7]
k=20
print(cntSubarrays(arr,k))