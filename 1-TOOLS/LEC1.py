# printing hello world 
print("Hello world ") 
'''/**********************************************************/'''
#variables
num_1 = 100 
MyName="AlaaElnaggar"
print(num_1)
print(MyName)
'''/***********************************************************/'''
#Using comma operator to define multiple variables in same line:
#Methods of injecting variables in string
F,S = 5 ,10
A,B = 3,4
# Method 1 
print("First number is {} and second number is {}".format(A, B))
# Method 2
print("First number is {first} and number is {second}".format(first=F, second=S)) 
# Method 3
print('First number is', F, 'second number is', S) 
# Method 4
print('First number %d and second number is %d' % (F, S))
# Method 5
print('First number is ' + str(F) + ' second number is '+ str(S))
'''/************************************************************/'''
#Input output
MyName = input ("Please Enter your name ") 
print ("My name is %d" %(MyName))
'''/***********************************************************/'''
#Receiving more than one variable
#input().split(separator, maxsplit)
# taking two inputs at a time  
 a, b, c = input("Enter three values: ").split("M",3)  
print("val1: ", a)  
print("val1: ", b)  
print("val1: ", c)  

print("Enter Your Last Name: ", b)  
print("Enter Your Class: ", c)  
print()  
   
#taking three inputs at a time  
x, y, z = input("Enter three values: ").split("p",3)  
print("Total number of students: ", x)  
print("Number of passed student : ", y)  
print("Number of failed student : ", z)  
   
# taking four inputs at a time with white space 
a, b, c, d = input("Enter four values: ").split()  
print("First number is {}, second number is {} third is {} and fourth is {}".format(a, b, c, d))    
'''/*******************************************************************************************/'''
#Type Casting in python
x = int("100")
print (x)
x = str (100)
print (x)
x = float (100)
print (x)
# printing asci value 
x=ord('A') 
print (x)
'''/***************************************************************************************/'''
# Arithmatic operators 
a = 90
b = 20
#addition 
print(a+b)
#subtraction
print(a-b)
#multiplication
print(a*b)
#divison
print(a/b)
#Exponentiation
print(a**b)
#floor divison
print(a//b)
#Modulas
print(a%b)
'''/***************************************************************************************/'''
# relational operators 
a = 5
b = 10
print(a == b)  #return False
print(a != b)  #return True
print(a < b)   #return True
print(a <= b)  #return True
print(a > b)   #return False
print(a >= b)  #return False
'''/***************************************************************************************/'''
# Bitwise operators in python 
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
c = a & b;        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101 
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)
'''/***************************************************************************************/'''
# Assignment Operators
a = 10
# Assign value
b = a
print(b)  #10
# Add and assign value
b += a  #20
print(b)
# Subtract and assign value
b -= a  #0
print(b)
# multiply and assign
b *= a  #100
print(b)
# bitwise lishift operator
b <<= a
print(b)
'''/***************************************************************************************/'''
Complex type
# Python complex() function example  
# Calling function  
a = complex(1) # Passing single parameter  
b = complex(1,2) # Passing both parameters  
# Displaying result  
print(a)  
print(b)
'''/***************************************************************************************/'''
'''Lists are used to store multiple items in a single variable.
Lists are created using square brackets:'''
#Creating lists

my_list = ['Alaa', 1, 5.4, 'Elnaggar', 0.7]

print(my_list)

#Accessing list values
print(my_list[2]) # 5.4

print(my_list[-1]) # 0.7
print(my_list[:2]) #  till element2

#Modifying lists
 x = "ITI"
Y = "567575I65767TI54667572" 
my_list.append(x) # append x to end of list
print(my_list)

my_list.extend(Y) # append all elements of Y to list
print(my_list)

my_list.insert(0, x) # insert x at index 1
print(my_list)

my_list.remove(x) # remove first occurance of x from list
print(my_list)

my_list.pop(3) # pop element at index i (defaults to end of list)
print(my_list)

my_list.clear() # delete all elements from the list
print(my_list)

my_list = ['Alaa', 1, 5.4, 'Elnaggar', 0.7,'Elnaggar']
x='Elnaggar'
print(my_list.index(x)) # return index of element x
print(my_list.count(x)) # return number of occurances of x in list
my_list.reverse() # reverse elements of list in-place (no return)
print(my_list)

my_list.sort(key=None, reverse=False) # sort list in-place
my_list.copy() # return a shallow copy of the list
my_nested_list = ['foobar', ['baz', 'qux'], [0]]
'''/***************************************************************************************/'''
'''Tuple
Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.

Ordered: it means that the items have a defined order, and that order will not change.
Unchangeable: we cannot change, add or remove items after the tuple has been created
Allow Duplicates: Since tuples are indexed, they can have items with the same value:'''
thistuple = ("apple", 2, "cherry",2)
print(thistuple)

# to print length of tuple 
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
print(thistuple[1])
#thistuple[1] = 1  # will produce error tuple is a constant 

# Tuble at least consist of two elements 
thistuple = ("apple",)
print(type(thistuple))
print(thistuple)

thistuple = ("apple")
print(type(thistuple)  ) 
'''/***************************************************************************************/'''
#Range
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default)
#and stops before a specified number
#range(start, stop, step)

x = range(1, 102 , 20)
for n in x:
    print(n)
    
x = range(6)
for n in x:
print(n)
'''/***************************************************************************************/'''
'''dict
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.'''

 thisdict = {
   "brand": "New",
  "model": "Bently",
  "year": 1964,
   "year": 2020
 }
 
 print(thisdict)

# Print the number of items in the dictionary:
 print(len(thisdict))

#The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(len(thisdict))

# printing dict elements 
print(thisdict["year"]) 
print(thisdict["colors"][1]) 
'''/***************************************************************************************/'''
'''set
A set is an unordered collection of items.
Every set element is unique(no duplicates) and must be immutable(cannot be changed).
a set itself is mutable. We can add or remove items from it.'''

# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set cannot have duplicates
# # Output: {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2])
print(my_set)

#set cannot have mutable items
#here [3, 4] is a mutable list
#this will cause an error.
# my_set = {1, 2, [3, 4]}

# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

my_set.add(100)
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
my_set.pop()
print(my_set)

# clear my_set
# Output: set()
my_set.clear()
print(my_set)
'''/***************************************************************************************/'''
'''The frozenset
function returns an immutable frozenset object initialized with elements from the given iterable.
Frozen set is just an immutable version of a Python set object.
While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
Due to this, frozen sets can be used as keys in Dictionary or as elements of another set.
But like sets, it is not ordered (the elements can be set at any index).'''
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)

# print('The frozen set is:', fSet[0]) # error 'frozenset' object is not subscriptable
# frozensets are immutable
# fSet.add('v') # error 
# fSet.remove(0)  # allowed in normal set
'''/***************************************************************************************/'''
