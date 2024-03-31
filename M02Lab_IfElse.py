last_name = input("Please enter student's last name: ")
if last_name == "ZZZ":
    exit()
first_name = input("Please enter student's first name: ")
gpa = float(input("Please enter students GPA: "))
if (gpa >= 3.5):
    print("Congratulations, ", first_name + " " + last_name,  "made the Dean's list!")
elif (gpa >= 3.25):
    print("Congratulations, ", first_name + " " + last_name, "made the Honor Roll")
else:
    print(first_name + last_name, "did not make the Dean's List or Honor Roll")

