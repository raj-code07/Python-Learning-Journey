nums=[1,2,3,4,5,6,7,8,9]
def even(x):
    v=[]
    for x in nums:
       if(x%2==0):
           v.append(x)
    return v
v=even(nums)
print(v)