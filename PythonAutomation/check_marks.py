marks_input = input("Enter marks: ")
marks = int(marks_input)

if marks < 0 or marks > 100:
    print("invalid number")
elif marks >=0 and marks <= 50:
    print("failed")
else:
    print("passed")