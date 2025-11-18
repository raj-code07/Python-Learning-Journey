nums=[1,2,3,4,5,6,7,]
def average(lst):
    total=0
    for x in lst:
        total += x
    return total/len(lst)
print(average(nums))
