def hIndex(citations):
    n=len(citations)
    freq=[0]*(n+1)
        
    for citations in citations:
        if citations>=n:
            freq[n]+=1
        else:
            freq[citations]+=1
                
    idx=n
    s=freq[n]
    while s<idx:
        idx-=1
        s+=freq[idx]
            
    return idx

citations = [6, 0, 3, 5, 3]
print(hIndex(citations))