from tkinter import *
import tkinter.messagebox
import stddb

class Student:
    def __init__(self,root):
        self.root =root
        self.root.title("student database management system")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        AdmissionNo=StringVar()
        StudentName=StringVar()
        Class=StringVar()
        DateOfBirth=StringVar()
        Age=StringVar()
        Gender=StringVar()
        Address=StringVar()
        ContactNo=StringVar()
        
        #============================Function=============================
        
        def iExit():
            iExit= tkinter.messagebox.askyesno("Students Database Management Systems","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
            
        def clearData():
            self.txtAdmissionNo.delete(0,END)
            self.txtStudentName.delete(0,END)
            self.txtClass.delete(0,END)
            self.txtDateOfBirth.delete(0,END)
            self.txtAge.delete(0,END)
            self.txtGender.delete(0,END)
            self.txtAddress.delete(0,END)
            self.txtContactNo.delete(0,END)

        def addData():
            if(len(AdmissionNo.get())!=0):
                stddb.addStdRec(AdmissionNo.get(), StudentName.get(), Class.get(), DateOfBirth.get(), Age.get(),Gender.get(), Address.get(), ContactNo.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(AdmissionNo.get(), StudentName.get(), Class.get(), DateOfBirth.get(), Age.get(),Gender.get(), Address.get(), ContactNo.get()))

        def DisplayData():
            studentlist.delete(0,END)
            for row in stddb.viewData():
                studentlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtAdmissionNo.delete(0,END)
            self.txtAdmissionNo.insert(END,sd[1])
            self.txtStudentName.delete(0,END)
            self.txtStudentName.insert(END,sd[2])
            self.txtClass.delete(0,END)
            self.txtClass.insert(END,sd[3])
            self.txtDateOfBirth.delete(0,END)
            self.txtDateOfBirth.insert(END,sd[4])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END,sd[5])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END,sd[6])
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END,sd[7])
            self.txtContactNo.delete(0,END)
            self.txtContactNo.insert(END,sd[8])

        def DeleteData():
            if(len(AdmissionNo.get())!=0):
                stddb.deleteRec(sd[0])
                clearData()
                DisplayData()

        def update():
            if(len(AdmissionNo.get())!=0):
                stddb.dataUpdate(sd[0],sd[1],sd[2],sd[3],sd[4],sd[5],sd[6],sd[7],sd[8])
            if(len(AdmissionNo.get())!=0):
                # stddb.addStdRec(AdmissionNo.get(), StudentName.get(), Class.get(), DateOfBirth.get(), Age.get(),Gender.get(), Address.get(), ContactNo.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(AdmissionNo.get(), StudentName.get(), Class.get(), DateOfBirth.get(), Age.get(),Gender.get(), Address.get(), ContactNo.get()))
                
        #============================Frames===============================
                
        MainFrame=Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2,padx=54,pady=8,bg="Ghost White", relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitleFrame= Label(TitleFrame, font=('arial',47,'bold'),text="Student Database Management System",bg="Ghost White")
        self.lblTitleFrame.grid()

        ButtomFrame = Frame(MainFrame, bd=2, width=1350,height=70, padx=18,pady=10,bg="Ghost White", relief=RIDGE)
        ButtomFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300,height=400, padx=20,pady=20, relief=RIDGE,bg="cadet blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000,height=600, padx=20, relief=RIDGE,bg="Ghost White",
                                   font=('arial',20,'bold'),text="Student Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450,height=300, padx=31,pady=3, relief=RIDGE,bg="Ghost White",
                                    font=('arial',20,'bold'),text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)
        
        #============================Labels and Entry Widget===============================
        
        self.lblAdmissionNo= Label(DataFrameLEFT, font=('arial',20,'bold'),text="AdmissionNo:",padx=2,pady=2,bg="Ghost White")
        self.lblAdmissionNo.grid(row=0,column=0,stick=W)
        self.txtAdmissionNo= Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=AdmissionNo,width=39)
        self.txtAdmissionNo.grid(row=0,column=1)

        self.lblStudentName= Label(DataFrameLEFT, font=('arial',20,'bold'),text="StudentName:",padx=2,pady=2,bg="Ghost White")
        self.lblStudentName.grid(row=1,column=0,stick=W)
        self.txtStudentName= Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=StudentName,width=39)
        self.txtStudentName.grid(row=1,column=1)

        self.lblClass= Label(DataFrameLEFT, font=('arial',20,'bold'),text="Class:",padx=2,pady=2,bg="Ghost White")
        self.lblClass.grid(row=2,column=0,stick=W)
        self.txtClass= Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=Class,width=39)
        self.txtClass.grid(row=2,column=1)

        self.lblDateOfBirth= Label(DataFrameLEFT, font=('arial',20,'bold'),text="DateOfBirth:",padx=2,pady=2,bg="Ghost White")
        self.lblDateOfBirth.grid(row=3,column=0,stick=W)
        self.txtDateOfBirth= Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=DateOfBirth,width=39)
        self.txtDateOfBirth.grid(row=3,column=1)

        self.lblAge= Label(DataFrameLEFT, font=('arial',20,'bold'),text="Age:",padx=2,pady=2,bg="Ghost White")
        self.lblAge.grid(row=4,column=0,stick=W)
        self.txtAge= Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=Age,width=39)
        self.txtAge.grid(row=4,column=1)

        self.lblGender= Label(DataFrameLEFT, font=('arial',20,'bold'),text="Gender:",padx=2,pady=2,bg="Ghost White")
        self.lblGender.grid(row=5,column=0,stick=W)
        self.txtGender= Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=Gender,width=39)
        self.txtGender.grid(row=5,column=1)

        self.lblAddress= Label(DataFrameLEFT, font=('arial',20,'bold'),text="Address:",padx=2,pady=2,bg="Ghost White")
        self.lblAddress.grid(row=6,column=0,stick=W)
        self.txtAddress= Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=Address,width=39)
        self.txtAddress.grid(row=6,column=1)

        self.lblContactNo= Label(DataFrameLEFT, font=('arial',20,'bold'),text="ContactNo:",padx=2,pady=2,bg="Ghost White")
        self.lblContactNo.grid(row=7,column=0,stick=W)
        self.txtContactNo= Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=ContactNo,width=39)
        self.txtContactNo.grid(row=7,column=1)

        #============================ListBox & ScrollBar Widget==================
        
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        studentlist=Listbox(DataFrameRIGHT,width=41,height=16,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command= studentlist.yview)

        
        #============================Button Widget===============================
        
        self.btnAddDate = Button(ButtomFrame, text="Add New",font=('arial',20,'bold'),height=1,width=10,bd=4,command=addData)
        self.btnAddDate.grid(row=0,column=0)
        self.btnDisplayData = Button(ButtomFrame, text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DisplayData)
        self.btnDisplayData.grid(row=0,column=1)
        self.btnClear = Button(ButtomFrame, text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4,command=clearData)
        self.btnClear.grid(row=0,column=2)
        self.btnDelete= Button(ButtomFrame, text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DeleteData)
        self.btnDelete.grid(row=0,column=3)
        self.btnUpdate = Button(ButtomFrame, text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4,command=update)
        self.btnUpdate.grid(row=0,column=5)
        self.btnExit = Button(ButtomFrame, text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=6)

if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
