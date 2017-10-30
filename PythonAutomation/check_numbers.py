number_input = input("Enter a number: ")
number = int(number_input)

if number <= 0:
    print("Invalid number")
elif number %2 == 0:
    print("even number")
else:
    print("odd number")
