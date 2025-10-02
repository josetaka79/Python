# Create a Python file named student.py. 
# In this file, define a dictionary student_info with keys 'name', 'age', and 'course'. 
# Access and print the value for 'name'. Then, add a key 'graduation_year' with the value 2023 
# and print the updated dictionary.
# Define the dictionary
student_info = {
    'name': 'Alice',
    'age': 22,
    'course': 'Computer Science'
}

# Access and print the value for 'name'
print(f"Name: {student_info['name']}")

# Add a new key-value pair for 'graduation_year'
student_info['graduation_year'] = 2023

# Print the updated dictionary
print(student_info)
##################################################################################################
# In the students.py file, start by creating an empty dictionary and then add key-value pairs 
# to it for a student's name, age, and major. Next, modify the student's age and major by 
# updating the values in the dictionary. Finally, remove the key-value pair for the student's major. 
# Make sure to print the dictionary after each modification to track the changes. 
# Additionally, use the get() method to access a student's age safely without causing an error 
# if the key is missing.
# Step 1: Create an empty dictionary
student_info = {}

# Step 2: Add key-value pairs for the student's information
student_info['name'] = 'John Doe'
student_info['age'] = 20
student_info['major'] = 'Computer Science'

# Print the dictionary after adding initial information
print(student_info)

# Step 3: Modify the student's age and major
student_info['age'] = 21
student_info['major'] = 'Data Science'

# Print the dictionary after modifying values
print(student_info)

# Step 4: Remove the key-value pair for the student's major
del student_info['major']

# Print the dictionary after removing the major
print(student_info)

# Step 5: Use get() to safely access the student's age
age = student_info.get('age', 'Age not available')
print(f"Student's age: {age}")


