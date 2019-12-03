from tkinter import *
import tkinter.messagebox
import LibBksDatabase

#===========Frontend========
class library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x750+0+0")


        MTy = StringVar()       #Member type
        Ref = StringVar()       #Reference No
        Tit = StringVar()       #Title
        Fna = StringVar()       #FirstName
        Sna = StringVar()       #Surname
        Adr1 = StringVar()      #Address 1
        Adr2 = StringVar()      #Address 2
        Pcd = StringVar()       #Post Code
        MNo = StringVar()       #Mobile No
        BkID = StringVar()      #Book ID
        Bkt = StringVar()       #Book Title
        Atr = StringVar()       #Author
        DBo = StringVar()       #Date Borrowed
        Ddu = StringVar()       #Date Due
        sPr = StringVar()       #Days On Loan
        LrF = StringVar()       #Late Return Fine
        DoD = StringVar()       #Date Over Due
        DonL = StringVar()      #Selling Price



#=============================FUNCTIONS=================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Management System", "Confirm if you want to Exit")
            if iExit > 0:
                root.destroy()
                return


        def ClearData():
            self.txtMType.delete(0, END)
            self.txtBkID.delete(0, END)
            self.txtRef.delete(0, END)
            self.txtBkt.delete(0, END)
            self.txtTit.delete(0, END)
            self.txtAtr.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtsna.delete(0, END)
            self.txtDdu.delete(0, END)
            self.txtAdr1.delete(0, END)
            self.txtAdr2.delete(0, END)
            self.txtDonL.delete(0, END)
            self.txtLrF.delete(0, END)
            self.txtpcd.delete(0, END)
            self.txtDoD.delete(0, END)
            self.txtMNo.delete(0, END)
            self.txtsPr.delete(0, END)
            self.txtDBo.delete(0, END)


        def AddData():
            if (len(MTy.get())!=0):
                LibBksDatabase.addDataRec(MTy.get(), Ref.get(), Tit.get(), Fna.get(),Sna.get(),
                                          Adr1.get(), Adr2.get(),Pcd.get(), MNo.get(), BkID.get(),
                                          Bkt.get(), Atr.get(), DBo.get(), Ddu.get(), sPr.get(),
                                          LrF.get(), DoD.get(), DonL.get())

                booklist.delete(0, END)
                booklist.insert(END, (MTy.get(), Ref.get(), Tit.get(), Fna.get(),Sna.get(),
                                          Adr1.get(), Adr2.get(),Pcd.get(), MNo.get(), BkID.get(),
                                          Bkt.get(), Atr.get(), DBo.get(), Ddu.get(), sPr.get(),
                                          LrF.get(), DoD.get(), DonL.get()))


        def DisplayData():
            booklist.delete(0, END)
            for row in LibBksDatabase.viewData():
                booklist.insert(END, row)


        def Selectedbook(event):
            global sb
            searchBk = booklist.curselection()[0]
            sb = booklist.get(searchBk)

            self.txtMType.delete(0, END)
            self.txtMType.insert(END, sb[1])
            self.txtBkID.delete(0, END)
            self.txtBkID.insert(END, sb[2])
            self.txtRef.delete(0, END)
            self.txtRef.insert(END, sb[3])
            self.txtBkt.delete(0, END)
            self.txtBkt.insert(END, sb[4])
            self.txtTit.delete(0, END)
            self.txtTit.insert(END, sb[5])
            self.txtAtr.delete(0, END)
            self.txtAtr.insert(END, sb[6])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END, sb[7])
            self.txtsna.delete(0, END)
            self.txtsna.insert(END, sb[8])
            self.txtDdu.delete(0, END)
            self.txtDdu.insert(END, sb[9])
            self.txtAdr1.delete(0, END)
            self.txtAdr1.insert(END, sb[10])
            self.txtAdr2.delete(0, END)
            self.txtAdr2.insert(END, sb[11])
            self.txtDonL.delete(0, END)
            self.txtDonL.insert(END, sb[12])
            self.txtLrF.delete(0, END)
            self.txtLrF.insert(END, sb[13])
            self.txtpcd.delete(0, END)
            self.txtpcd.insert(END, sb[14])
            self.txtDoD.delete(0, END)
            self.txtDoD.insert(END, sb[15])
            self.txtMNo.delete(0, END)
            self.txtMNo.insert(END, sb[16])
            self.txtsPr.delete(0, END)
            self.txtsPr.insert(END, sb[17])
            self.txtDBo.delete(0, END)
            self.txtDBo.insert(END, sb[18])


        def DeleteData():
            if (len(MTy.get()) != 0):
                LibBksDatabase.deleteRec(sb[0])
                ClearData()
                DisplayData()

        def searchDatabase():
            booklist.delete(0, END)
            for row in LibBksDatabase.searchData(MTy.get(),Ref.get(),Tit.get(),Fna.get(),Sna.get(),
                                                 Adr1.get(),Adr2.get(),Pcd.get(),MNo.get(),BkID.get(),
                                                 Bkt.get(),Atr.get(),DBo.get(),
                                                 Ddu.get(),sPr.get(),LrF.get(),DoD.get(),DonL.get()):
                booklist.insert(END, row)


        def update():
            if (len(MTy.get()) != 0):
                LibBksDatabase.dataUpdate(sb[0],MTy.get(),Ref.get(),Tit.get(),Fna.get(),Sna.get(),
                                                 Adr1.get(),Adr2.get(),Pcd.get(),MNo.get(),BkID.get(),
                                                 Bkt.get(),Atr.get(),DBo.get(),
                                                 Ddu.get(),sPr.get(),LrF.get(),DoD.get(),DonL.get())



#==================================FRAMES================================
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=40, pady=8, bg="Cadet blue", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=("arial", 46, "bold"), text="Library Management System")
        self.lblTit.grid(stick=W)

        Buttonframe = Frame(MainFrame, width=1350, bd=2, height=100, padx=20, pady=20, bg="Cadet blue", relief=RIDGE)
        Buttonframe.pack(side=BOTTOM)

        Framedetail = Frame(MainFrame, width=1350, bd=0, height=50, padx=20, pady=20, relief=RIDGE)
        Framedetail.pack(side=BOTTOM)

        Dataframe = Frame(MainFrame, width=1350, bd=0, height=400, padx=20, pady=20, relief=RIDGE)
        Dataframe.pack(side=BOTTOM)

        DataframeLEFT = LabelFrame(Dataframe, width=800, bd=1, height=300, padx=20, relief=RIDGE,
                              font=("arial", 12, "bold"), text="Library Membership Intel", bg="Cadet Blue")
        DataframeLEFT.pack(side=LEFT)

        DataframeRIGHT = LabelFrame(Dataframe, width=450, bd=1, height=300, padx=20, pady=3, relief=RIDGE,
                              font=("arial", 12, "bold"), text="Book Details", bg="Cadet Blue")
        DataframeRIGHT.pack(side=RIGHT)
#=================================Label and Entry===================================
        self.lblMemberType = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Member Type", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblMemberType.grid(row=0, column=0, sticky=W)
        self.txtMType = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=MTy, width=25)
        self.txtMType.grid(row=0, column=1, sticky=W)


        self.lblBkID = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Book ID:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblBkID.grid(row=0, column=2, sticky=W)
        self.txtBkID = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=BkID, width=25)
        self.txtBkID.grid(row=0, column=3, sticky=W)



        self.lblRef = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Reference No:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=Ref, width=25)
        self.txtRef.grid(row=1, column=1, sticky=W)



        self.lblBkt = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Book Title:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblBkt.grid(row=1, column=2, sticky=W)
        self.txtBkt = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=Bkt, width=25)
        self.txtBkt.grid(row=1, column=3, sticky=W)



        self.lblTit = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Title:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblTit.grid(row=2, column=0, sticky=W)
        self.txtTit = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=Tit, width=25)
        self.txtTit.grid(row=2, column=1, sticky=W)



        self.lblAtr = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Author:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblAtr.grid(row=2, column=2, sticky=W)
        self.txtAtr = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=Atr, width=25)
        self.txtAtr.grid(row=2, column=3, sticky=W)



        self.lblfna = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Firstname", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblfna.grid(row=3, column=0, sticky=W)
        self.txtfna = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=Fna, width=25)
        self.txtfna.grid(row=3, column=1, sticky=W)



        self.lblDBo = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Date Borrowed:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblDBo.grid(row=3, column=2, sticky=W)
        self.txtDBo = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=DBo, width=25)
        self.txtDBo.grid(row=3, column=3, sticky=W)



        self.lblsna = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Surname:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblsna.grid(row=4, column=0, sticky=W)
        self.txtsna = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=Sna, width=25)
        self.txtsna.grid(row=4, column=1, sticky=W)



        self.lblDdu = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Date Due:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblDdu.grid(row=4, column=2, sticky=W)
        self.txtDdu = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=Ddu, width=25)
        self.txtDdu.grid(row=4, column=3, sticky=W)



        self.lblAdr1 = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Address 1:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblAdr1.grid(row=5, column=0, sticky=W)
        self.txtAdr1 = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=Adr1, width=25)
        self.txtAdr1.grid(row=5, column=1, sticky=W)



        self.lblDonL = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Date on Loan:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblDonL.grid(row=5, column=2, sticky=W)
        self.txtDonL = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=DonL, width=25)
        self.txtDonL.grid(row=5, column=3, sticky=W)



        self.lblAdr2 = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Address 2:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblAdr2.grid(row=6, column=0, sticky=W)
        self.txtAdr2 = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=Adr2, width=25)
        self.txtAdr2.grid(row=6, column=1, sticky=W)



        self.lblLrF = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Late Return Fine:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblLrF.grid(row=6, column=2, sticky=W)
        self.txtLrF = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=LrF, width=25)
        self.txtLrF.grid(row=6, column=3, sticky=W)



        self.lblpcd = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Post Code:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblpcd.grid(row=7, column=0, sticky=W)
        self.txtpcd = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=Pcd, width=25)
        self.txtpcd.grid(row=7, column=1, sticky=W)



        self.lblDoD = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Date Over Due:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblDoD.grid(row=7, column=2, sticky=W)
        self.txtDoD = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=DoD, width=25)
        self.txtDoD.grid(row=7, column=3, sticky=W)



        self.lblMNo = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Mobile No:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblMNo.grid(row=8, column=0, sticky=W)
        self.txtMNo = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=MNo, width=25)
        self.txtMNo.grid(row=8, column=1, sticky=W)



        self.lblsPr = Label(DataframeLEFT, font=('arial', 12, 'bold'), text="Selling Price:", padx=2, pady=2,
                                   bg="Cadet Blue")
        self.lblsPr.grid(row=8, column=2, sticky=W)
        self.txtsPr = Entry(DataframeLEFT, font=('arial', 12, 'bold'), textvariable=sPr, width=25)
        self.txtsPr.grid(row=8, column=3, sticky=W)


#========================================List BOX AND SCROLL BAR===============================================
        scrollbar = Scrollbar(DataframeRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        booklist = Listbox(DataframeRIGHT, width=45, height=12, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>', Selectedbook)
        booklist.grid(row=0, column=0, padx=8)
        scrollbar.configure(command=booklist.yview)

#=========================================Buttons Widget===============================================================

        self.btnAddData = Button(Buttonframe, text='Add Data', font=('arial', 14, 'bold'), height=2, width=13, bd=4, command=AddData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(Buttonframe, text='Display Data', font=('arial', 14, 'bold'), height=2, width=14, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(Buttonframe, text='Clear Data', font=('arial', 14, 'bold'), height=2, width=13, bd=4, command=ClearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(Buttonframe, text='Delete Data', font=('arial', 14, 'bold'), height=2, width=14, bd=4, command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnUpdataData = Button(Buttonframe, text='Update Data', font=('arial', 14, 'bold'), height=2, width=14, bd=4, command=update)
        self.btnUpdataData.grid(row=0, column=4)

        self.btnSearchData = Button(Buttonframe, text='Search Data', font=('arial', 14, 'bold'), height=2, width=14, bd=4, command=searchDatabase)
        self.btnSearchData.grid(row=0, column=5)

        self.btnExit = Button(Buttonframe, text='Exit', font=('arial', 14, 'bold'), height=2, width=13, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)









if __name__ == "__main__":
    root = Tk()
    application = library(root)
    root.mainloop()
