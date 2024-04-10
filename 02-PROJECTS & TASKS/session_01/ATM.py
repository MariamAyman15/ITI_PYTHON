print("Welcome To ATM Machine")
PIN = int(input("Enter Your Pin: "))
BAL = 25000
if (PIN == 1234):
	print("1-WithDraw")
	print("2-Balance Enquiry")
	print("3-Fast Cash")

c = int(input("Please Enter Transaction: "))
 
if(c == 1):
	w = int(input("Enter WithDraw Amout: "))
	if((w < BAL) and (w%100 == 0)):
		print("Please Take Your Amount...")
	else:
		print("Invalid Cash!")

elif(c == 2):
	print("Your Avaliable Amout: ",BAL)
elif(c == 3):
	print("1->5,000")
	print("2->10,000")
	print("3->15,000")
	f = int(input("Enter Fast Cash Option: "))
	if((f == 1) and (5000 < BAL)):
		print("Please Take 5000 Cash")
	elif((f == 2) and (10000 < BAL)):
		print("Please Take 10000 Cash")
	elif((f == 3) and (15000 < BAL)):
		print("Please Take 15000 Cash")
	else:
		print("Wrong Option")	