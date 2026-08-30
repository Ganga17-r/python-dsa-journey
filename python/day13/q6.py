# Q6 — First EVEN number
num = [15, 27, 33, 41, 52, 68, 75]
for i in range(len(num)):
    if num[i]%2==0:
        print("First even number 😁: ",num[i])
        break

else:
    print("No even number found😥")