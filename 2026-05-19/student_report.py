# Student Details

name = "John Doe"
age = 28
# Marks in 3 subjects stored in a list
marks = [78.5, 85.0, 67.5]

student_details = {
    "name": name,
    "age": age,
    "marks": marks
}

# Print Student Details

print("Student Details:")
print(f"Name: {student_details['name']}")
print(f"Age: {student_details['age']}")
print(f"Marks: {student_details['marks']}") 

# Print Variable Types

def var_types(std):
    print(f"Name: {std['name']} (Type: {type(std['name'])})")
    print(f"Age: {std['age']} (Type: {type(std['age'])})")
    print(f"Marks: {std['marks']} (Type: {type(std['marks'])})")   

print("\nVariable Types:")
var_types(student_details)

# Print Mark Details

Total = sum(student_details['marks'])
Average =sum(student_details['marks']) / len(student_details['marks'])
print("\nTotal Marks:", Total)
print("Average Marks:", Average)
print("Pass/Fail Status:", "PASS" if Average>=40 else "FAIL")

print("\nIndividual Marks: ")
for i, mark in enumerate(student_details['marks']):
    print(f"Subject {i + 1}: {mark}")

markSet = set(student_details['marks'])
print("\nMarks Set:", markSet)

subjects = ("Mathematics", "Science", "English")
print("\nSubjects: ", subjects)

remarks = None
print("\nType of remarks variable:", type(remarks))

ispassed = Average >= 40
print("\nIs Passed:", ispassed)


#Formatted Student Report
print("\n============Formatted Student Report: ==============")

print(f"Student Name: {student_details['name']}")
print(f"Age: {student_details['age']} years")
print("Marks:")
for i, mark in enumerate(student_details['marks']):
    print(f"  Subject {i + 1}: {mark}")
print(f"Total Marks: {Total}")
print(f"Average Marks: {Average:.2f}")
print(f"Pass/Fail Status: {'PASS' if ispassed else 'FAIL'}")
print("Remarks: ", "Excellent" if Average >= 85 else "Good" if Average >= 70 else "Needs Improvement" if Average >= 40 else "Poor")

print("===============================================")    

