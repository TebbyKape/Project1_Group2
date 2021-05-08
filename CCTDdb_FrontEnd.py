from tkinter import*
import tkinter.messagebox
import CCTDdb_BackEnd
import datetime

#windows = Tk()

class Patient:
    def __init__(self, root):
        
        
        self.root = root
        self.root.title("Covid Contact Tracing Database Management System")
       #width= window.winfo_screenwidth() 
       #height= window.winfo_screenheight()
        root.overrideredirect(True)
        root.overrideredirect(False)
        root.attributes('-fullscreen',True)
        #self.root.geometry("%dx%d" % (width,height))
        self.root.config(bg="cadet blue")

        PntID = StringVar ()
        Firstname = StringVar ()
        Surname = StringVar ()
        DoB= StringVar()
        Age = StringVar ()
        Gender = StringVar ()
        Address = StringVar ()
        MoNo = StringVar ()
        LastPersonContact=StringVar()
        DateIssued = StringVar()

        #==========================FUNCTION================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Covid Contact Tracing Database Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData(): #delete(0,END)
            self.txtPntID.set("")
            self.txtfna.set("")
            self.txtSna.set("")
            self.txtDob.set("")
            self.txtAge.set("")
            self.txtGender.set("")
            self.txtAdr.set("")
            self.txtMoNo.set("")
            self.txtLastPC.set("")
            self.txtRecordings.delete("1.0",END)

        def addData():
            if(len(PntID.get())!=0) :
                CCTDdb_BackEnd.AddPntRec(PntID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), \
                        MoNo.get(), LastPersonContact.get())
                Patientlist.delete(0,END)
                Patientlist.insert(END,PntID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), \
                        MoNo.get(), LastPersonContact.get())
            DateIssued.set(time.strftime("%d/%m/%Y"))
            self.txtRecordings.insert(END,'Patient ID:\t\t' + PntID.get() + '\t\t' + DateIssued.get() + "\n")


        def displayData():
            Patientlist.delete(0,END)
            for row in CCTDdb_BackEnd.viewData():
                Patientlist.insert(END,row, str(""))

        def PatientRec(event):
            global sd
            searchPnt = Patientlist.curselection()[0]
            sd=Patientlist.get(searchPnt)

            self.txtPntID.delete(0,END)
            self.txtPntID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtSna.delete(0,END)
            self.txtSna.insert(END,sd[3])
            self.txtDob.delete(0,END)
            self.txtDob.insert(END,sd[4])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END,sd[5])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END,sd[6])
            self.txtAdr.delete(0,END)
            self.txtAdr.insert(END,sd[7])
            self.txtMoNo.delete(0,END)
            self.txtMoNo.insert(END,sd[8])
            self.txtLastPC.delete(0,END)
            self.txtLastPC.insert(END,sd[9])

        def deleteData():
            if(len(PntID.get())!=0):
                CCTDdb_BackEnd.deleteRec(sd[0])
                clearData()
                displayData()

        def SearchData():
            Patientlist.delete(0,END)
            for row in CCTDdb_BackEnd.searchData(PntID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(),\
               MoNo.get(), LastPersonContact.get()):
                Patientlist.insert(END,row,str(""))

        def update():
            if (len(PntID.get())!=0):
                CCTDdb_BackEnd.deleteRec(sd[0])
            if(len(PntID.get())!=0):
                CCTDdb_BackEnd.AddPntRec(PntID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), \
                        MoNo.get(), LastPersonContact.get())
                Patientlist.delete(0,END)
                Patientlist.insert(END,PntID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), \
                        MoNo.get(), LastPersonContact.get())

    #=========================FRAME=================================
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        #TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        #TitFrame.pack(side=TOP)

        #self.lblTit = Label(TitFrame, font=('arial', 47,'bold'),text="CCTD Management Systems", bg="Ghost White")
        #self.lblTit.grid()
        
        DataFrame2 = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
        DataFrame2.pack(side=BOTTOM)

        ListFrame = LabelFrame(DataFrame2, bd=2, width=1350, height=180, padx=18, pady=10, relief=RIDGE, bg="Ghost White",
                                    font=('Arial', 20,'bold'), text="Patient List Details\n")
        ListFrame.pack(side=TOP)
        
        ButtonFrame = Frame(DataFrame2, bd=2, width=1350, height=40, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
        DataFrame.pack(side=TOP)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=900, height=200, padx=20, pady=6, relief=RIDGE, bg="Ghost White",
                                   font=('Arial', 18,'bold'), text="Patient Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=200, padx=31, pady = 9, relief=RIDGE, bg="Ghost White",
                                   font=('Arial', 18,'bold'), text="Records\n")
        DataFrameRIGHT.pack(side=RIGHT)
        
        #==================Recordings==================
        self.txtRecordings = Text (DataFrameRIGHT, height = 13, width=43, bd=1, font=('arial', 11, 'bold'))
        self.txtRecordings.grid(row=0, column=0)

        #==================Labels and Entry Widget==================
        self.lblPntID = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Patient ID:",padx=2, pady=2,bg="Ghost White")
        self.lblPntID.grid(row=0, column=0, sticky=W)
        self.txtPntID = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=PntID,width=28)
        self.txtPntID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="First Name:",padx=2, pady=2,bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=Firstname,width=28)
        self.txtfna.grid(row=1, column=1)

        self.lblSna = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Surname:",padx=2, pady=2,bg="Ghost White")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=Surname,width=28)
        self.txtSna.grid(row=2, column=1)

        self.lblDob = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Date of Birth:",padx=2, pady=2,bg="Ghost White")
        self.lblDob.grid(row=3, column=0, sticky=W)
        self.txtDob = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=DoB,width=28)
        self.txtDob.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Age:",padx=2, pady=2,bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=Age,width=28)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Gender:",padx=2, pady=2,bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=Gender,width=28)
        self.txtGender.grid(row=5, column=1)

        self.lblAdr = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Address:",padx=2, pady=2,bg="Ghost White")
        self.lblAdr.grid(row=6, column=0, sticky=W)
        self.txtAdr = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=Address,width=28)
        self.txtAdr.grid(row=6, column=1)

        self.lblMoNo = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Mobile No:",padx=2, pady=2,bg="Ghost White")
        self.lblMoNo.grid(row=7, column=0, sticky=W)
        self.txtMoNo = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=MoNo,width=28)
        self.txtMoNo.grid(row=7, column=1)

        self.lblLastPC = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Last Person Contact:",padx=2, pady=2,bg="Ghost White")
        self.lblLastPC.grid(row=8, column=0, sticky=W)
        self.txtLastPC = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=LastPersonContact,width=28)
        self.txtLastPC.grid(row=8, column=1)

        #===================================ListBox & ScrollBar Widget==================================
        scrollbar = Scrollbar(ListFrame)
        scrollbar.grid(row=0, column=1, sticky='ns')

        Patientlist = Listbox(ListFrame, width=141, height=7, font=('Arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        Patientlist.bind('<<ListboxSelect>>', PatientRec)
        Patientlist.grid(row=0, column=0, padx=9)
        scrollbar.config(command = Patientlist.yview)

        #===================================Button Widget==================================
        self.btnAddData = Button(ButtonFrame, text="Add New",font=('Arial', 12, 'bold'), height=1, width=16, bd=2, padx=13, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display",font=('Arial', 12, 'bold'), height=1, width=16, bd=2, padx=9, command=displayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear",font=('Arial', 12, 'bold'), height=1, width=16, bd=2, padx=9, command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete",font=('Arial', 12, 'bold'), height=1, width=16, bd=2, padx=9, command=deleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search",font=('Arial', 12, 'bold'), height=1, width=16, bd=2, padx=9, command=SearchData)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update",font=('Arial', 12, 'bold'), height=1, width=16, bd=2, padx=9, command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit",font=('Arial', 12, 'bold'), height=1, width=16,bd=2, padx=12, command = iExit)
        self.btnExit.grid(row=0, column=6)


if __name__=='__main__':
    root = Tk() 
    application = Patient (root)
    root.mainloop()


