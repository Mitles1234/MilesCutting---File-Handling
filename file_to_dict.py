# TODO: Open "student_data.txt" in read mode
Students = {}
with open("student_age.txt", "r") as file:
    # Read lines from the file and store them in a list
    Student_Data = file.readlines()

for line in Student_Data:
    Name, Age = line.strip().split(",") # TODO: For each line, split line into name and age (separated by comma)
    Students[Name] = int(Age)  # TODO: Store in the dictionary with the name as the key and age as the value

# TODO: Print the dictionary
print(Students)
