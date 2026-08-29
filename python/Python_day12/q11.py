#11Q-Find the total of all valid expenses.
expenses = [500, -100, 250, 0, 700, -50, 300]
total=0
for i in range(len(expenses)):
    if expenses[i]<=0:
        continue
    total=total+expenses[i]
print(total)