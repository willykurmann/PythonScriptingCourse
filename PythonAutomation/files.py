f = open("file1.txt","r")
# print(f.read()) # read all file
# print(f.readline()) # read one line at a time
print(f.read(10)) # read number of characters in the file
f.close()

f = open("file1.txt","a")
f.write("\nthis is next data")
f.close()

f = open("file1.txt","r+")
print(f.read(10))
print(f.tell())
print(f.seek(15))
print(f.tell())
f.close()