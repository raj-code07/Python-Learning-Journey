# - Write code that accesses a key "marks" and prints its value if it exists,
#  else prints "Key not found" using if key in dict.


student={"name":"raj","age":19,"roll":101}
key="marks"
if key in student:
    print("marks",student[key])
else:
    print("key not found")