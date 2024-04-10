#capitalize() , find() , isalpha() , startswith()
while True:
	print("1:capitalize(), 2:find(), 3:isalpha, 4:startswith()")
	print("enter your choice: ")
	choice = int(input())
	if choice == 1 :
			cap = '''The capitalize(): it returns a string where the first character is upper case, and the rest is lower case.
				Exampe:
				txt = "hello, and welcome to my world."
				x = txt.capitalize()
				print (x)'''
			print(cap)
		
	elif choice == 2:
			find = '''The find() method finds the first occurrence of the specified value.
				Exampe:
				txt = "Hello, welcome to my world."
				x = txt.find("welcome")
				print(x)
				'''
			print(find)
		
	elif choice == 3:
		alpha = '''The isalpha():returns True if all the characters are alphabet letters (a-z).
				Example of characters that are not alphabet letters: (space)!#%&? etc.
				Exampe:
				txt = "CompanyX"
				x = txt.isalpha()
				print(x)'''
		print(alpha)
		
	elif choice == 4:
		start = '''startswith(): it returns True if the string starts with the specified value,otherwise False.
				Example:
				txt = "Hello, welcome to my world."
				x = txt.startswith("Hello")
				print(x)'''
		print(start)
		
	elif (choice > 4):
		print("error")


