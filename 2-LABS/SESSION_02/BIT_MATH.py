#set bit function
def SET_BIT_FUNC(VAR,BIT_NUM):
	VAR = int(VAR)
	BIT_NUM = int(BIT_NUM)
	result = VAR | (1 << BIT_NUM)
	return result

#clear bit function	
def CLR_BIT_FUNC(VAR,BIT_NUM):
	VAR = int(VAR)
	BIT_NUM = int(BIT_NUM)
	result = VAR & (~(1 << BIT_NUM))
	return result

#git bit function	
def GET_BIT_FUNC(VAR,BIT_NUM):
	VAR = int(VAR)
	BIT_NUM = int(BIT_NUM)
	result = (VAR >> BIT_NUM) & 1
	return result

#toggle bit function	
def TOG_BIT_FUNC(VAR,BIT_NUM):
	VAR = int(VAR)
	BIT_NUM = int(BIT_NUM)
	result =VAR ^ (1 << BIT_NUM) 
	return result


print("enter number:")
VAR = int(input())
print("enter bit number:")
BIT_NUM = int(input())

print("set bit: ")
print(SET_BIT_FUNC(VAR,BIT_NUM))

print("clear bit")
print(CLR_BIT_FUNC(VAR,BIT_NUM))

print("get bit")
print(GET_BIT_FUNC(VAR,BIT_NUM))

print("toggle bit")
print(TOG_BIT_FUNC(VAR,BIT_NUM))