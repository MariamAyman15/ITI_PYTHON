# Import all methods of the module  
from tkinter import *
'''
def func():
	print("mariam marioma")

window_1 = Tk()

#add title
window_1.title("Hello!")

#control window_1 geometry in pixels
window_1.geometry('500x500')

#add label
label_1 = Label(window_1,text = "ITI LAB")
label_1.pack(side = BOTTOM)
label_1 = Label(window_1 , text = "iti lab" ,background="light green" , fg="yellow" , font = ('Verdana', 15)).pack(side=BOTTOM)

#add button in top

#b1 = Button(window_1,text = "HELLO")

#call the function
#b1 = Button(window_1,text= "func print", bd= '10',command = func)

#close the window_1
#b1 = Button(window_1,text= "close", bd= '10',command = window_1.destroy)


#load image
photo_1 = PhotoImage(file='cat.png')
photo_1 = photo_1.subsample(2,2)
b1 = Button(window_1,text= "image", bd= '5',image = photo_1,command = func)
b1.place(x=250,y=250)

#add button in right
b2 = Button(window_1,text = "OTHER SIDE!",background="light green" , fg="black" )
b2.pack(side = RIGHT)

#add button in LEFT
b3 = Button(window_1,text = "FROM THE",background="light green" , fg="black" )
b3.pack(side = LEFT)
'''
top = Tk()
#geometry size 
top.geometry('300x100')
#var to store data
name_var = StringVar()
pass_var = StringVar()

#create function
def submit():
	name=name_var.get()
	password=pass_var.get()
	
	print("The name is : " + name)
	print("The password is : " + password)
	
	name_var.set("")
	pass_var.set("")
	
#name abel
name_label = Label(top, text = 'Username', font=('calibre',10, 'bold'))
# name using widget Entry
name_entry = Entry(top,textvariable = name_var, font=('calibre',10,'normal'))
pass_label = Label(top, text = 'Password', font = ('calibre',10,'bold'))
# creating an entry for password
pass_entry=Entry(top, textvariable = pass_var, font = ('calibre',10,'normal'))
# Button that will call the submit function
sub_btn=Button(top,text = 'Submit', command = submit)
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
pass_label.grid(row=1,column=0)
pass_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
'''L1.pack(side= LEFT)
E1 = Entry(top,bd=5)
E1.pack(side=RIGHT)'''
top.mainloop()