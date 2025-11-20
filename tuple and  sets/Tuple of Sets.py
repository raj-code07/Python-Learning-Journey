# - Create a tuple containing two sets.
# - Access and modify the sets inside the tuple.

tup=({1,2,3,4},{6,7,8})
print("first set:",tup[0])
print("second set:",tup[1])

tup[0].add(5)
tup[1].discard(8)
print(tup)