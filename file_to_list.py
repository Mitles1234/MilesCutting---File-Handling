# TODO: Open the file "students.txt" in read mode
Students = []
with open("students.txt", "r") as file:
    Students = file.readlines() # TODO: Read lines from the file and store them in a list


#TODO: Remove extra spaces and newlines from each name. Use list comprehension to STRIP whitespace
for Index, Name in enumerate(Students): # I found this cool
    Students[Index] = Name.strip()

# TODO: Print the list
    # TODO: Print the cleaned-up list

print(Students)
