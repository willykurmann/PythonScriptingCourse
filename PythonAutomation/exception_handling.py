first_mark = input("enter first mark:")
second_mark = input("enter second mark:")

try:
    print(int(first_mark) + int(second_mark))
except:
    print("marks are incorrects")
finally:
    print("closing this execution")