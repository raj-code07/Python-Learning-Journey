def computelps(pat, m, lps):
    length=0
    lps[0]=0
    i=1
    while i<m:
        if pat[i]==pat[length]:
            length+=1
            lps[i]=length
            i+=1
        else:
            if length!=0:
                length=lps[length-1]
            else:
                lps[i]=0
                i+=1
                        
def search(pat, txt):
    n=len(txt)
    m=len(pat)
    lps=[0]*m
    res=[]
    computelps(pat, m, lps)
    i=0
    j=0
    while i<n:
        if txt[i]==pat[j]:
            i+=1
            j+=1
            if j==m:
                res.append(i-j)
                j=lps[j-1]
                    
        else:
            if j!=0:
                j=lps[j-1]
                    
            else:
                i+=1
    return res

txt = "aabaacaadaabaaba"
pat = "aaba"

res = search(pat, txt)
for i in range(len(res)):
    print(res[i], end=" ")