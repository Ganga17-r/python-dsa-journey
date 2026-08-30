# Q5 — Find the first number greater than 50
num= [12, 25, 38, 17, 63, 71, 45, 90]
for i in range(len(num)):
    if num[i]>50:
        print("First number greater than 50:",num[i])
        break
else:
    print("No number greater than 50 ")
