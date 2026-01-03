def intersect(a, b):
    sa=set(a)
    res=[]
    for ele in b:
        if ele in sa:
            res.append(ele)
            sa.remove(ele)
                
    return res
        
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

res = intersect(a, b)
print(" ".join(map(str,res)))