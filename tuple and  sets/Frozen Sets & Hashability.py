# - Create a frozenset from a list.
# - Try using it as a dictionary key.
nums=[1,2,3,4]
fs=frozenset(nums)
print(fs)
my_dict={fs:"this is a frozenset"}
print(my_dict[fs])


# - frozenset is an immutable version of set — once created, it cannot be changed.
# - Because it's immutable, it is hashable and can be used as:
# - Dictionary keys
# - Set elements (nested sets)
# - Normal set is not hashable, so it cannot be used as a key
