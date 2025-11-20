set={1,2,3,4,3,2,1}
set.add(5)
# set.add(1)add nhi krta 1 pehle se h
set.remove(4)  # Works fine
# set.remove("4")  # ❌ Will raise KeyError if 

set.discard(3)  # ✅ No error even if not present

print(set)
