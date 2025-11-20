# - From a list of numbers, create a set of squares using set comprehension.
lst=[1,2,3,4,5,6,7,8,9]
set={i**2 for i in lst}
print(set)