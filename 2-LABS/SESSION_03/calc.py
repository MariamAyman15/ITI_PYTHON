import os

#print("enter the first number: ")
a = int(input("enter the first number: "))

print("enter the operation: ")
print("1 -> '+' , 2 -> '-' , 3 -> '*' , 4 -> '/' ")
op = int(input())

#print("enter the second number: ")
b = int(input("enter the second number: "))

#create file
f1 = open("file2.txt","a+")

if op == 1 :
	print("sum = ",a+b)
	#write in this file
	f1.write(str(a+b))
	f1.write("\n")
elif op == 2 :
	print("sub = ",a-b)
	f1.write(str(a-b))
	f1.write("\n")
elif op == 3 :
	print("multi = ",a*b)
	f1.write(str(a*b))
	f1.write("\n")
elif op == 4 :
	print("div = ",a/b)
	f1.write(str(a/b))
	f1.write("\n")
#close
f1.close()
#read
f1 = open("file2.txt","r")
print(f1.read())

#print(f2.readlines()) #read as list by line
#os.remove()
