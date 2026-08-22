# Project: Expense Tracker
# Version: 1 - Python Foundation
print("=" * 40)#Display a clean header
print("        EXPENSE TRACKER")
print("=" * 40)
total = 0
for i in range(3):#Handle 3 expenses
  print("----- Expense", i + 1, "-----")
  expense_name=input("Enter expense name:")#Take expense name
  expense_amount=float(input("enter expense amount:"))#Take expense amount
  if expense_amount > 0:#Add valid expenses to a running total
    print("Valid expense amount")
    total = total + expense_amount
  else:
    print("Invalid expense amount")#Reject negative amounts from the total
    
      
  expense_category=input("Enter expense category: ")#Take category
  
  print("expense:",expense_name)
  print("Amount:",expense_amount)
  print("category:" ,expense_category)
print("=" * 40)#Display the final total
print("Total Expense:", total)
print("=" * 40)




