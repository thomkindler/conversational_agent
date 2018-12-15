



#unsuccesful try
try:
   fh = open("gugus", "r")
   a=fh.readlines()
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()


##succesful try
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()


#raise an eception
level=10
if level <12:
    raise Exception("This is my exception")
      # The code below to this would not be executed
      # if we raise the exception
print("Hallo")


#assertion ohne Fehlermeldung
def avg(marks):
    assert len(marks) != 0
    return sum(marks)/len(marks)

mark1 = []
print("Average of mark1:",avg(mark1))

#assertion mit Fehlermeldung
def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

mark1 = []
print("Average of mark1:",avg(mark1))

