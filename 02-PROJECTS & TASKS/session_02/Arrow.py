import os
import time
import shutil

n = 9

while True:
    # Wait for input (1 or 2)
    choice = input("Enter 1 or 2: ")

    # Calculate centering whitespace
    term_size = shutil.get_terminal_size()
    whitespace = " " * ((term_size.columns - n*2) // 2)

    if choice == "1":
        #right
        cc = (n-1)*2
        for i in range(1,n):
            print(whitespace + ' '*(cc)+'*')
            cc += 2
        print(whitespace + '* '*((n-1)*2))
        cc1 = n*4-6
        for i in range(n-1,0,-1):
            print(whitespace + ' '*(cc1)+'*')
            cc1 -=2
        time.sleep(1)
        os.system('cls')

        #down
        for i in range(n-1):
            print(whitespace + '  '*n+'*')
        for j in range(1,n):
            print(whitespace + '  '*(j-1)+'* '+'  '*(n-j)+'*'+'  '*(n-j)+' *')
        print(whitespace + '  '*n+'*')
        time.sleep(1)
        os.system('cls')

        #left
        for i in range(1,n):
            print(whitespace + ' '*((n-i)*2)+'*')
        print(whitespace + '* '*(n*2-1))
        for i in range(n-1,0,-1):
            print(whitespace + ' '*((n-i)*2)+'*')
        time.sleep(1)
        os.system('cls')

        #up
        print(whitespace + '  '*n+'*')
        for i in range(n-1,0,-1):
            print(whitespace + '  '*(i-1)+'* '+'  '*(n-i)+'*'+'  '*(n-i)+' *')
        for j in range(n-1):
            print(whitespace + '  '*n+'*')
        time.sleep(1)
        os.system('cls')

    elif choice == "2":
        #up
        print(whitespace + '  '*n+'*')
        for i in range(n-1,0,-1):
            print(whitespace + '  '*(i-1)+'* '+'  '*(n-i)+'*'+'  '*(n-i)+' *')
        for j in range(n-1):
            print(whitespace + '  '*n+'*')
        time.sleep(1)
        os.system('cls')

        #left
        for i in range(1,n):
            print(whitespace + ' '*((n-i)*2)+'*')
        print(whitespace + '* '*(n*2-1))
        for i in range(n-1,0,-1):
            print(whitespace + ' '*((n-i)*2)+'*')
        time.sleep(1)
        os.system('cls')

        #down
        for i in range(n-1):
            print(whitespace + '  '*n+'*')
        for j in range(1,n):
            print(whitespace + '  '*(j-1)+'* '+'  '*(n-j)+'*'+'  '*(n-j)+' *')
        print(whitespace + '  '*n+'*')
        time.sleep(1)
        os.system('cls')

        #right
        cc = (n-1)*2
        for i in range(1,n):
            print(whitespace + ' '*(cc)+'*')
            cc += 2
        print(whitespace + '* '*((n-1)*2))
        cc1 = n*4-6
        for i in range(n-1,0,-1):
            print(whitespace + ' '*(cc1)+'*')
            cc1 -=2
        time.sleep(1)
        os.system('cls')