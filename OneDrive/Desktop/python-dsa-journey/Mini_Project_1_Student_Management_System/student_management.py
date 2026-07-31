#Ask the user for:
'''Student Name
Marks
Attendance Percentage'''

student_name=input("student name:")
marks=int(input("Marks:"))
attendence=int(input("Attendence:"))
print("=" * 40)
print("       STUDENT MANAGEMENT SYSTEM             ")
print("=" * 40)
print("----------- STUDENT DETAILS -----------")
print("Student Name :", student_name)
print("Marks        :", marks)
print("Attendance   :", attendence, "%")
#------------------PHASE 2------------------
print("-------------RESULT--------------------")
if marks>=35:
    result="PASS"
else:
    result="FAIL"
print("Result      :",result)
# ------------------ PHASE 3 ------------------

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 50:
    grade = "C"

else:
    grade = "F"

print("Grade        :", grade)
#-------------------- Phase 4------------------
if marks>=75 and attendence>=80:
    scholarship= "APPROVED 🎉"
else:
    scholarship="NOT APPROVED ❌"
print("Scholarship  :",scholarship)
#------------------- Phase 5 ------------------
print("=" * 40)