# - Remove the "roll" key using .pop() and print the removed value
# - pop("roll") us key ko dictionary se hata dega aur uska value return karega


student={"name":"raj","age":19,"roll":101}
removed_value=student.pop("roll")
print("removed roll:",removed_value)

print("updated dic.:",student)