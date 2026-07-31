#problem-15
'''Problem Statement
A college wants to provide a scholarship to students.
Write a Python program that asks the user to enter:Student Name
Marks (out of 100)
Attendance Percentage
📜 Rules
A student gets the scholarship only if:
Marks are 75 or above
AND
Attendance is 80% or above
If Eligible
Print:
Congratulations <Student Name>!
Scholarship Approved 🎉
Otherwise
Print:
Sorry <Student Name>.
Scholarship Not Approved'''
student_name=input("Enter your name:")
marks=int(input("Enter your marks:"))
attendance_percentage=int(input("enter your attendence percentage:"))
if marks>=75 and attendance_percentage>=80:
    print("Congratulations",student_name)
    print("Scholarship Approved 🎉")
else:
    print("Sorry",student_name)
    print("Scholarship Not Approved")

          