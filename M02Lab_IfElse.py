# Sahajpreet Singh
# 3/31/2024
# M02 Lab - If Else and while
# Program determines whether a student has made the Honor roll,
# Dean's list, neither or both.


last_name = input("Please enter student's last name: ")
if last_name == "ZZZ":
    exit()
# The previous line could also be:
# While last_name == "ZZZ":
#   break   
# But the assignment said "if the last name is 'ZZZ' so I took it literally" 
first_name = input("Please enter student's first name: ")
gpa = float(input("Please enter students GPA: "))
if (gpa >= 3.5):
    print("Congratulations, ", first_name + " " + last_name,  "made the Dean's list!")
elif (gpa >= 3.25):
    print("Congratulations, ", first_name + " " + last_name, "made the Honor Roll")
else:
    print(first_name + last_name, "did not make the Dean's List or Honor Roll")
