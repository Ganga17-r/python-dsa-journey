# Q7 — First VALID expense
expenses = [-50, -20, 0, -10, 250, 300, 150]
for i in range(len(expenses)):
    if expenses[i]>0:
        print('First valid expense: ',expenses[i])
        break
else:
    print('No valid expense found')