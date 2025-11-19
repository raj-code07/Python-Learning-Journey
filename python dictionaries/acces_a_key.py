# Access a key "grade" from the dictionary using .
#get() and print "Not found" if it doesn’t exist

student={"name":"raj","age":19,"grade":"A"}
grade=student.get("grade","not found")
print(grade)
