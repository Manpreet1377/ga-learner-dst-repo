# --------------
# Code starts here

# Create the lists 
print("STEP 1: CREATING A REGISTER")
class_1 = ["Geoffrey Hinton", "Andrew Ng", "Sebastian Raschka", "Yoshua Bengio"]
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class = class_1 + class_2
print("This is the concatenated class")
print(new_class)

# Append the list
new_class.append("Peter Warden")

# Print updated list
print("Peter is added here")
print(new_class)

# Remove the element from the list
new_class.remove("Carla Gentry")

# Print the list
print("Carla is removed")
print(new_class)
print("="*40)

# Create the Dictionary
print("STEP 2: DICTIONARY FOR GEOFFERY HINTON")
courses = {"Math":65, "English":70, "History":80, "French":70, "Science":60}
print(courses)

# Slice the dict and stores  the all subjects marks in variable
Math = courses["Math"]
English = courses["English"]
History = courses["History"]
French = courses["French"]
Science = courses["Science"]

# Store the all the subject in one variable `Total`
Total = Math + English + History + French + Science

# Print the total
print("This is  Geoffery's total marks: {}".format(Total))

# Insert percentage formula
print("This is Geoffery Hinton's percentage: {}".format(Total*0.2))

# Print the percentage
print("="*40)

# Create the Dictionary
print("STEP 3: DICTIONARY FOR SCHOLARSHIP")
mathematics = {"Geoffery Hinton":78, "Andrew Ng":95, "Sebastian Raschka":65, "Yoshua Benjio":50, "Hilary Mason":70, "Corinna Cortes":66, "Peter Warden":75}
max_marks_math = max(mathematics, key = mathematics.get)
print("Student who scored maximum marks in Maths: {}".format(max_marks_math))
topper = max_marks_math
print("="*40)

# Given string
print("STEP 4:PRINT CERTIFICATE")

# Create variable first_name 
first_name = topper.split()[0]

# Create variable Last_name and store last two element in the list
last_name = topper.split()[1]

# Concatenate the string
full_name = last_name + " " + first_name

# print the full_name
print("Certificate name:" + " " + full_name)

# print the name in upper case
certificate_name = full_name.upper()
print("PRINT THIS NAME ON THE CERTIFICATE:" + " " + certificate_name)
# Code ends here


