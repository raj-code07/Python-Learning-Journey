def findUnion(a, b):
    st=set()
        
    for i in range(len(a)):
        st.add(a[i])
            
    for i in range(len(b)):
        st.add(b[i])
            
    res=[]
    for it in st:
        res.append(it)
        
    return res

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

res = findUnion(a, b)

for value in res:
    print(value, end=" ")