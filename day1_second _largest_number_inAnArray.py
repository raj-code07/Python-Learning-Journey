arr = [12, 35, 1, 10, 33, 1]

def get2num(arr):
    if len(arr)<2:
        return -1
    
    i1=i2=float('-inf')

    for num in arr:
        if i1<num:
            i2=i1
            i1=num
           
        elif num > i2 and num != i1:
            i2=num
    if i2 == float('-inf'):
        return -1
    else:
        return i2

print(get2num(arr))
