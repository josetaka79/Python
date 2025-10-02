#create an empty dictionary
student={}
print("Initial dictionary:", student)

#Add key-value pairs (name, age, major)
student["name"] = "Alice"
student["age"] = 20
student["major"] = "Computer science"
print("After adding details:", student)

# Modify the student's age and major
student["age"] = 21
student["major"] ="Data Science"
print("After updating age and major:", student)

# Removing the key-value pair for major
del student["major"]
print("After removing major:", student)

# use get() to safely access age
age = student.get("age")
print("student's age(using get):", age)

# Try to get a misiing key safely (e.g. , GPA)
gpa= student.get("gpa", "Not available")
print("student's GPA (using get):", gpa)
