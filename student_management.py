print("===== Student =====")

name = input("Enter student Name: ")
roll_no = input("Enter Roll Number: ")
marks = int(input("Enter Marks: "))

print("\n----- Student Details-----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Marks:", marks)

if marks >= 50:
    print("Result: pass")
else:
    print("Result: fail")