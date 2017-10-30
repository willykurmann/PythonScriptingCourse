s = 'String declaration "Part of string"\n'
print(s)

s = "This is Testing' World\n"
print(s)

s = """Only use to declare
Multiple lines\n"""
print(s)

s = "Testing"
print(s[0]) # display character at position 0
print(s[1:4]) # substring from 1 to 6 location
print(s[1:]) # substring from left to end
print(s[:4]) # substring from start to position 4
print(s * 5) # repetition
print("")

s = "  Testing  "
print(len(s))
print(s)
print(s.lstrip()) # remove whitespaces from start
print(s.rstrip()) # remove whitespaces from end
print(s.strip()) # remove whitespaces from both start and end
print("")

s = "TesTinG"
print(s.upper())
print(s.lower())
print(s.replace("es", "35"))
print(s.find("es")) # index of substring
print(s.find("ES")) # index of substring -1 = not found
print("")

s = "This is testing world"
li = s.split(" ")
print(li)
print(len(li))
print(li[0])
print(li[2:])
print("")

#string compare
s = "hello"
s1 = "hello"
if(s==s1):
    print ("equal")
else:
    print("not equal")

