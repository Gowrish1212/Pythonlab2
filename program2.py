
students = {}


num_students = int(input("Enter the number of students: "))


for i in range(num_students):
    print(f"\nEntering data for student {i + 1}:")
    roll_number = input("Enter roll number: ")
    name = input("Enter name: ")
    
    
    students[roll_number] = name


print("\nStudent Dictionary:")
for roll_no, name in students.items():
    print(f"Roll Number: {roll_no}, Name: {name}")
