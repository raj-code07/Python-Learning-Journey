# Day 07 - Weekly Project 01
# Daily Task Organizer

# Step 1: Subah ke tasks
tasks = []  # empty list
n = int(input("Aaj ke total tasks kitne hain? "))

for i in range(n):
    task = input(f"Task {i+1} likho: ")
    tasks.append(task)

print("\nAaj ke tasks:")
for t in tasks:
    print("-", t)

# Step 2: Shaam ko poochho kaunse complete hue
completed = []
incomplete = []

for task in tasks:
    done = input(f"Kya '{task}' complete hua? (yes/no): ").lower()
    if done == "yes":
        completed.append(task)
    else:
        incomplete.append(task)

# Step 3: Result dikhao
print("\n✅ Completed Tasks:")
for c in completed:
    print("-", c)

print("\n❌ Incomplete Tasks:")
for i in incomplete:
    print("-", i)

print("\nGreat! Tumne apna din organize kar liya 😄")