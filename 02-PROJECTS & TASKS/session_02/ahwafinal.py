### Importing required libraries ###
from tkinter import *
import random
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import *
import pygame 
from playsound import playsound

#It is definition of System
def system():
    root = Tk()
    root.geometry("1700x800")
    root.title("El - AHWA ")
    pygame.mixer.init()
    root.config(bg='white')
    img = PhotoImage(file="aa.png")
    label = Label(root,image=img)
    label.place(x=460, y=0)


    def play():
        playsound('safsf.mp3')

    def Database():
        global connectn, cursor
        connectn = sqlite3.connect("Restaurant.db")
        cursor = connectn.cursor()
        # creating bill table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Restaurantrecords(ordno text,piz text,bur text,ice text, dr text, ct text,sb text,tax text,sr text,tot text)")

    # variable datatype assignment
    orderno = StringVar()
    Shay    = StringVar()
    ahwaa   = StringVar()
    omALi   = StringVar()
    pepsi   = StringVar()
    shisha  = StringVar()
    Limon   = StringVar()
    Sa7lab  = StringVar()
    Zbadi   = StringVar()
    total   = StringVar()

    # defining total function
    def tottal():
        # fetching the values from entry box
        order = (orderno.get())
        Sha   = float(Shay.get())
        ahw   = float(ahwaa.get())
        oma   = float(omALi.get())
        pp    = float(pepsi.get())
        shi   = float(shisha.get())
        Lim   = float(Limon.get())
        Sah   = float(Sa7lab.get())
        Zba   = float(Zbadi.get())

        # computing the cost of items
        costSha = Sha * 7
        costahw = ahw * 10
        costoma = oma * 30
        costpp  = pp  * 10
        costshi = shi * 15
        costlim = Lim * 10
        costsah = Sah * 20
        costzba = Zba * 12

        # computing the charges
        costofmeal = (costSha + costahw + costoma + costpp + costshi + costlim + costsah + costzba )
        overall = str(costofmeal)

        # Displaying the values
        total.set(overall)

    # defining reset function
    def reset():
        orderno.set("")
        Shay.set("")
        ahwaa.set("")
        omALi.set("")
        pepsi.set("")
        shisha.set("")
        Limon.set("")
        Sa7lab.set("")
        Zbadi.set("")
        total.set("")

    # defining exit function
    def exit():
        root.destroy()

    # Topframe
    topframe = Frame(root, bg="white", width=1600, height=50)
    topframe.config(bg='white')
    topframe.pack(side=TOP)

    # Leftframe
    leftframe = Frame(root, width=900, height=700)
    leftframe.config(bg='white')
    leftframe.pack(side=LEFT)

    # rightframe
    rightframe = Frame(root, width=400, height=700)
    rightframe.config(bg='white')
    rightframe.pack(side=RIGHT)

    ################## display data ####################
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.execute("SELECT * FROM Restaurantrecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    style = ttk.Style()
    style.configure("Treeview",
                    foreground="black",
                    rowheight=40,
                    fieldbackground="white"
                    )
    style.map('Treeview',
              background=[('selected', 'lightblue')])

    ###########  Creating table #############
    my_tree = ttk.Treeview(rightframe)
    my_tree['columns'] = ("ordno", "piz", "bur", "ice", "dr", "ct", "sb", "tax", "sr", "tot")

    ############ creating  for table ################
    horizontal_bar = ttk.Scrollbar(rightframe, orient="horizontal")
    horizontal_bar.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=horizontal_bar.set)
    horizontal_bar.pack(fill=X, side=BOTTOM)

    vertical_bar = ttk.Scrollbar(rightframe, orient="vertical")
    vertical_bar.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vertical_bar.set)
    vertical_bar.pack(fill=Y, side=RIGHT)

    # defining column for table
    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("ordno", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("piz", anchor=CENTER, width=60, minwidth=25)
    my_tree.column("bur", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ice", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("dr", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ct", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sb", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tax", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sr", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tot", anchor=CENTER, width=50, minwidth=25)

    # defining  headings for table
    my_tree.heading("ordno", text="Order No", anchor=CENTER)
    my_tree.heading("piz", text="Shay", anchor=CENTER)
    my_tree.heading("bur", text="ahwaa", anchor=CENTER)
    my_tree.heading("ice", text="Om ALI", anchor=CENTER)
    my_tree.heading("dr", text="Pepsi", anchor=CENTER)
    my_tree.heading("ct", text="shisha", anchor=CENTER)
    my_tree.heading("sb", text="Limon", anchor=CENTER)
    my_tree.heading("tax", text="Sa7lab", anchor=CENTER)
    my_tree.heading("sr", text="Zbadi", anchor=CENTER)
    my_tree.heading("tot", text="Cost", anchor=CENTER)

    my_tree.pack()
    DisplayData()

    # defining add function to add record
    def add():
        Database()
        # getting  data
        orders = orderno.get()
        Shays = Shay.get()
        ahwaas = ahwaa.get()
        omas = omALi.get()
        pepsis = pepsi.get()
        shishas = shisha.get()
        limons = Limon.get()
        sa7labs = Sa7lab.get()
        zbadis = Zbadi.get()
        totals = total.get()
        if orders == "" or Shays == "" or ahwaas == "" or omas == "" or pepsis == "" or shishas == "" or limons == "" or sa7labs == "" or zbadis == "" or totals == "":
            messagebox.showinfo("Warning", "Please fill the empty field !")
        else:
            connectn.execute(
                'INSERT INTO Restaurantrecords (ordno, piz, bur , ice ,dr ,ct ,sb ,tax, sr, tot) VALUES (?,?,?,?,?,?,?,?,?,?)',
                (orders, Shays, ahwaas, omas, pepsis, shishas, limons, sa7labs, zbadis, totals));
            connectn.commit()
            messagebox.showinfo("Message", "Stored successfully")
        # refresh table data
        DisplayData()
        connectn.close()

    # defining function to access data from sqlite datrabase
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.execute("SELECT * FROM Restaurantrecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    # defining function to delete record
    def Delete():
        # open database
        Database()
        if not my_tree.selection():
            messagebox.showwarning("Warning", "Select data to delete")
        else:
            result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                            icon="warning")
        if result == 'yes':
            curItem = my_tree.focus()
            contents = (my_tree.item(curItem))
            selecteditem = contents['values']
            my_tree.delete(curItem)
            cursor = connectn.execute("DELETE FROM Restaurantrecords WHERE ordno= %d" % selecteditem[0])
            connectn.commit()
            cursor.close()
            connectn.close()

    # Time
    localtime = time.asctime(time.localtime(time.time()))
    # Top part
    main_lbl = Label(topframe, font=('Calibri', 25, 'bold'), text="Ahwet Hadota", fg="Blue",
                   anchor=W)
    main_lbl.grid(row=0, column=0)
    main_lbl.config(bg='white')

    main_lbl = Label(topframe, font=('Calibri', 15,), text=localtime, fg="green", anchor=W)
    main_lbl.grid(row=1, column=0)

    ### Labels
    #Bt3'yer l Gdwl l 3l shmal
    # items
    ordlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Order No.", fg="black", bd=5, anchor=W).grid(row=1,
                                                                                                             column=0)
    ordtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=orderno).grid(row=1, column=1)
    # Shay
    shalbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Shay", fg="black", bd=5, anchor=W).grid(row=2,
                                                                                                         column=0)
    shatxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=Shay).grid(row=2, column=1)
    # Ahwa
    ahwlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="ahwaa", fg="black", bd=5, anchor=W).grid(row=3,
                                                                                                          column=0)
    ahwtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=ahwaa).grid(row=3, column=1)

    # Om Ali
    omlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Om ALi", fg="black", bd=5, anchor=W).grid(row=4,
                                                                                                             column=0)
    omtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=omALi).grid(row=4, column=1)
    # pepsi
    drinklbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Pepsi", fg="black", bd=5, anchor=W).grid(row=5,
                                                                                                            column=0)
    drinktxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                     textvariable=pepsi).grid(row=5, column=1)
    # shisha
    costlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Shisha", bd=5, anchor=W).grid(row=6, column=0)
    costtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                    textvariable=shisha).grid(row=6, column=1)
    # Limon
    sublbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Limon", bd=5, anchor=W).grid(row=7, column=0)
    subtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=Limon).grid(row=7, column=1)
    # sa7lab
    taxlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Sa7lab", bd=5, anchor=W).grid(row=8, column=0)
    taxtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=Sa7lab).grid(row=8, column=1)
    # zbadi
    servicelbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Zbadi", bd=5, anchor=W).grid(row=9,
                                                                                                              column=0)
    servicetxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                       textvariable=Zbadi).grid(row=9, column=1)
    # total
    totallbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Cost", bd=5, anchor=W).grid(row=10,
                                                                                                          column=0)
    totaltxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                     textvariable=total).grid(row=10, column=1)
    # ---button--

    # making a button which trigger the function so sound can be playeed

    playbtn = Button(leftframe, font = ('Calibri', 16, 'bold'), text = "Start", bg="Lightgrey",fg="black",bd=3,padx=5, pady=5,
                      width=6,command=play).grid(row= 8,column=3)

    totbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Total", bg="Lightgrey", fg="black", bd=3, padx=5, pady=5,
                    width=6, command=tottal).grid(row=6, column=3)

    resetbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Reset", bg="lightgrey", fg="black", bd=3, padx=5,
                      pady=5, width=6, command=reset).grid(row=4, column=3)

    exitbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Exit The System", bg="lightgrey", fg="black", bd=3, padx=5,
                     pady=5, width=12, command=exit).grid(row=6, column=2)

    addbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Add", bg="lightgrey", fg="black", bd=3, padx=5, pady=5,
                    width=6, command=add).grid(row=2, column=3)

    deletebtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Delete Record", bg="lightgrey", fg="black", bd=3,
                       padx=5, pady=5, width=12, command=Delete).grid(row=4, column=2)

    ########################### feedback form ################################

    def feedbackk():
        feed = Tk()
        feed.geometry("600x500")
        feed.title("Submit Feedback form")
        # database #
        connectn = sqlite3.connect("Restaurant.db")
        cursor = connectn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS FEEDBACK(n text,eid text,feedback5 text,com text)")
        # variable datatype asssignment #
        name = StringVar()
        email = StringVar()
        comments = StringVar()

        # defiing submit function
        def submit():
            n = name.get()
            eid = email.get()
            com = txt.get('1.0', END)
            feedback1 = ""
            feedback2 = ""
            feedback3 = ""
            feedback4 = ""
            if (checkvar1.get() == "1"):
                feedback1 = "Kolo Bono ?"
            if (checkvar2.get() == "1"):
                feedback2 = "Good"
            if (checkvar3.get() == "1"):
                feedback2 = "Average"
            if (checkvar4.get() == "1"):
                feedback2 = "Poor"
            feedback5 = feedback1 + " " + feedback2 + " " + feedback3 + " " + feedback4
            conn = sqlite3.connect("Restaurant.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO FEEDBACK VALUES ('" + n + "','" + eid + "','" + com + "','" + feedback5 + "')")
            messagebox.showinfo("message", "data inserted !")
            feed.destroy()

        # defining cancel button
        def cancel():
            feed.destroy()

        # label#
        lb1 = Label(feed, font=("Calisto MT", 15, "bold"), text="Msa2k 3enab", fg="black").pack(side=TOP)
        lbl2 = Label(feed, font=("calisto MT", 15), text="T3ala Ya Handsa Ahwetk Gahza",
                     fg="black").pack(side=TOP)
        # name
        namelbl = Label(feed, font=('vardana', 15), text="Name:-", fg="black", bd=10, anchor=W).place(x=10, y=150)
        nametxt = Entry(feed, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                        textvariable=name).place(x=15, y=185)
        # email
        emaillbl = Label(feed, font=('vardana', 15), text="Email:-", fg="black", bd=10, anchor=W).place(x=280, y=150)
        emailtxt = Entry(feed, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                         textvariable=email).place(x=285, y=185)
        ###checkbutton
        ratelbl = Label(feed, font=('vardana', 15), text="Eh L Kalam", fg="black", bd=10, anchor=W).place(
            x=10, y=215)
        checkvar1 = StringVar()
        checkvar2 = StringVar()
        checkvar3 = StringVar()
        checkvar4 = StringVar()
        c1 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="Kolo Bono!", bg="white", variable=checkvar1)
        c1.deselect()
        c1.place(x=15, y=265)
        c2 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="Sh3'al", bg="white", variable=checkvar2, )
        c2.deselect()
        c2.place(x=120, y=265)
        c3 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="Msh Ad Kda", bg="white", variable=checkvar3, )
        c3.deselect()
        c3.place(x=220, y=265)
        c4 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="L M3asl Bayz", bg="white", variable=checkvar4, )
        c4.deselect()
        c4.place(x=320, y=265)
        # comments"
        commentslbl = Label(feed, font=('Calibri', 15), text="Comments", fg="black", bd=10, anchor=W).place(x=10, y=300)
        txt = Text(feed, width=50, height=5)
        txt.place(x=15, y=335)
        # button
        submit = Button(feed, font=("Calibri", 15), text="Submit", fg="black", bg="green", bd=2, command=submit).place(
            x=145, y=430)
        cancel = Button(feed, font=("Calibri", 15), text="Cancel", fg="black", bg="red", bd=2, command=cancel).place(
            x=245, y=430)
        feed.mainloop()


    # Feedbackbutton
    feedbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Feedback Form", fg="black", bg="lightgrey", bd=3, padx=5,
                     pady=5, width=12, command=feedbackk).grid(row=8, column=2, columnspan=1)

    ##################### Menu card ################################
    def menu():
        roott = Tk()
        roott.title("Price Menu")
        roott.geometry("300x300")
        lblinfo = Label(roott, font=("Calibri", 20, "bold"), text="ITEM LIST", fg="black", bd=10)
        lblinfo.grid(row=0, column=0)
        lblprice = Label(roott, font=("Calibri", 20, "bold"), text="Prices", fg="black", bd=10)
        lblprice.grid(row=0, column=3)
        lblshay = Label(roott, font=("Calibri", 20, "bold"), text="Shay", fg="Blue", bd=10)
        lblshay.grid(row=1, column=0)
        lblpricep = Label(roott, font=("Calibri", 20, "bold"), text="7/-", fg="blue", bd=10)
        lblpricep.grid(row=1, column=3)
        lblburger = Label(roott, font=("Calibri", 20, "bold"), text="ahwaa", fg="Blue", bd=10)
        lblburger.grid(row=3, column=0)
        lblpriceb = Label(roott, font=("Calibri", 20, "bold"), text="10/-", fg="blue", bd=10)
        lblpriceb.grid(row=3, column=3)
        lblicecream = Label(roott, font=("Calibri", 20, "bold"), text="Om ALi", fg="Blue", bd=10)
        lblicecream.grid(row=4, column=0)
        lblpricei = Label(roott, font=("Calibri", 20, "bold"), text="30/-", fg="blue", bd=10)
        lblpricei.grid(row=4, column=3)
        lbldrinks = Label(roott, font=("Calibri", 20, "bold"), text="Pepsi", fg="Blue", bd=10)
        lbldrinks.grid(row=5, column=0)
        lblpriced = Label(roott, font=("Calibri", 20, "bold"), text="10/-", fg="blue", bd=10)
        lblpriced.grid(row=5, column=3)
        lblshisha = Label(roott, font=("Calibri", 20, "bold"), text="Shisha", fg="Blue", bd=10)
        lblshisha.grid(row=6, column=0)
        lblpriced = Label(roott, font=("Calibri", 20, "bold"), text="15/-", fg="blue", bd=10)
        lblpriced.grid(row=6, column=3)
        lblshisha = Label(roott, font=("Calibri", 20, "bold"), text="Limon", fg="Blue", bd=10)
        lblshisha.grid(row=7, column=0)
        lblpriced = Label(roott, font=("Calibri", 20, "bold"), text="10/-", fg="blue", bd=10)
        lblpriced.grid(row=7, column=3)
        lblshisha = Label(roott, font=("Calibri", 20, "bold"), text="Sa7lab", fg="Blue", bd=10)
        lblshisha.grid(row=8, column=0)
        lblpriced = Label(roott, font=("Calibri", 20, "bold"), text="20/-", fg="blue", bd=10)
        lblpriced.grid(row=8, column=3)
        lblshisha = Label(roott, font=("Calibri", 20, "bold"), text="Zbadi", fg="Blue", bd=10)
        lblshisha.grid(row=9, column=0)
        lblpriced = Label(roott, font=("Calibri", 20, "bold"), text="12/-", fg="blue", bd=10)
        lblpriced.grid(row=9, column=3)
        roott.mainloop()

    # menubutton
    menubtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Menu Card", bg="lightgrey", fg="black", bd=3, padx=6,
                     pady=6, width=12, command=menu).grid(row=2, column=2)

    root.mainloop()


system()