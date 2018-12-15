
#input von User
x = input("something:")
print(x)

# Open a file for writing
# r: Opens a file for reading only. The file pointer is placed at the beginning of the file
# w: Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing
# a: Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")
fo.close()

# Open a file for reading
fo = open("foo.txt", "r")
str = fo.read()
print ("Read String is : ", str)

# Close opened file
fo.close()


# Open a file for reading line by line
fo = open("foo.txt", "r")
lines = fo.readlines()
fo.close()
print(lines)


# Open a file for reading line by line
fo = open("foo.txt", "r")
line = fo.readline()
while (line):
    print ("Read String is : ", line)
    line = fo.readline()
fo.close()