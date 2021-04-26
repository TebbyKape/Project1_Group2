from tkinter import*
import tkinter.messagebox
#import stdDatabase

class Patient:
    def __init__(self, root):
        self.root = root
        self.root.title("Covid Contact Tracing Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")
        
        StdID = StringVar ()
        Firstname = StringVar ()
        Surname = StringVar ()
        Age = StringVar ()
        Gender = StringVar ()
        Address = StringVar ()
        Mobile = StringVar ()
        #=========================FRAME=================================
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47,'bold'),text="CCTD Management Systems", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="Ghost White",
                                   font=('arial', 20,'bold'), text="Patient Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg="Ghost White",
                                    font=('arial', 20,'bold'), text="Patient Details\n")
        DataFrameRIGHT.pack(side=RIGHT)
        #==================Labels and Entry Widget==================
        self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Patient ID:",padx=2, pady=2,bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID,width=39)
        self.txtStdID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="First Name:",padx=2, pady=2,bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID,width=39)
        self.txtfna.grid(row=1, column=1)

        self.lblSna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Surname:",padx=2, pady=2,bg="Ghost White")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID,width=39)
        self.txtSna.grid(row=2, column=1)

        self.lblDob = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date of Birth:",padx=2, pady=2,bg="Ghost White")
        self.lblDob.grid(row=3, column=0, sticky=W)
        self.txtDob = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID,width=39)
        self.txtDob.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age:",padx=2, pady=2,bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID,width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender:",padx=2, pady=2,bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID,width=39)
        self.txtGender.grid(row=5, column=1)

        self.lblSna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Surname:",padx=2, pady=2,bg="Ghost White")
        self.lblSna.grid(row=6, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID,width=39)
        self.txtSna.grid(row=6, column=1)

        self.lblSna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Surname:",padx=2, pady=2,bg="Ghost White")
        self.lblSna.grid(row=7, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID,width=39)
        self.txtSna.grid(row=7, column=1)
        



if __name__=='__main__':
    root = Tk() 
    application = Patient (root)
    root.mainloop()


