import os
#create file
f1 = open("file.txt","w") 
#write in this file
f1.write("My name is mariam /n")
f1.write("i'm 24 Years old")
#read
f1 = open("file.txt","r")
print(f1.read())
#close
f1.close()
#print(f2.readlines()) #read as list by line
os.remove()