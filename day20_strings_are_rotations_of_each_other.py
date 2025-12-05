
def computeRotations(pat):
        n=len(pat)
        lps=[0]*n
        patLen=0
        lps[0]=0
        i=1
        while i<n:
            if pat[i]==pat[patLen]:
                patLen+=1
                lps[i]=patLen
                i+=1
            else:
                if patLen!=0:
                    patLen=lps[patLen-1]
                    
                else:
                    lps[i]=0
                    i+=1
        return lps
    
    
def areRotations(s1, s2):
        if len(s1) != len(s2):
            return False
        txt=s1+s1
        pat=s2
        n=len(txt)
        m=len(pat)
        lps=computeRotations(pat)
        i=0
        j=0
        while i<n:
            if txt[i]==pat[j]:
                j+=1
                i+=1
            if j==m:
                return True
            elif i<n and  txt[i] != pat[j]:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return False

s1 = "aab" 
s2 = "aba"
print("true" if areRotations(s1, s2) else "false")