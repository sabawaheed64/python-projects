print("===== Student Grade Management System =====")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
marks= int(input("Enter Marks: "))

if marks >= 90:
    grade ="A"

elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("\n----- Student Report -----")
print("Name:", name)
print("Roll Number:", roll)
print("Marks:", marks)
print("Grade:", grade)

if marks >=50:
    print("Result: Pass")
else:
    print("Result: Fail")
    