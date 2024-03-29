from tkinter import* #for gui application
from tkinter import ttk
from PIL import Image,ImageTk#for image crop fix
from tkinter import messagebox#for show message
import os
import csv
from tkinter import filedialog
mydata=[]

class Attendance:
    def __init__(self,root):#construction call (root =window name(1st self))
        self.root=root#initialize
        self.root.geometry("1080x720+0+0")#(width,height,x start from 0,y start form 0)
        self.root.title("Face Recognition Attendance System")

        #============== Variables ==============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #background img
        img3=Image.open(r"imges\stubg.jpg")
        img3=img3.resize((1530,790),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        #title
        title_n=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("sans-serif",35,"bold"),bg="black",fg="yellow")
        title_n.place(x=0,y=0,width=1530,height=70)

        #main frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=90,width=1390,height=750)

        #left label fram
        left_inside_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text="Student Attendaance Details",font=("times new roman",12,"bold"),fg="blue")
        left_inside_frame.place(x=10,y=10,width=650,height=680)

        #first image
        img_left=Image.open(r"imges\students.jpg")
        img_left=img_left.resize((510,150),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg=ImageTk.PhotoImage(img_left)
        
        f_lb=Label(left_inside_frame,image=self.photoimg)
        f_lb.place(x=120,y=440,width=400,height=150)


        # labels and entry
        #Attendance ID
        attendanceId_label=Label(left_inside_frame,text="AttendanceId",font=("times new roman",12,"bold"),fg="red")
        attendanceId_label.grid(row=9,column=0,padx=10,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),textvariable=self.var_atten_id)
        attendanceId_entry.grid(row=9,column=1,padx=2,pady=10,sticky=W)
        
        #Roll no
        rollLable=Label(left_inside_frame,text="Roll no",font=("times new roman",12,"bold"),fg="red")
        rollLable.grid(row=11,column=0,padx=10,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),textvariable=self.var_atten_roll)
        atten_roll.grid(row=11,column=1,padx=2,pady=10,sticky=W)

        #Name
        nameLable=Label(left_inside_frame,text="Name",font=("times new roman",12,"bold"),fg="red")
        nameLable.grid(row=13,column=0,padx=10,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),textvariable=self.var_atten_name)
        atten_name.grid(row=13,column=1,padx=2,pady=10,sticky=W)


        #department
        depLable=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"),fg="red")
        depLable.grid(row=15,column=0,padx=10,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),textvariable=self.var_atten_dep)
        atten_dep.grid(row=15,column=1,padx=2,pady=10,sticky=W)


        #time
        timeLable=Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"),fg="red")
        timeLable.grid(row=17,column=0,padx=10,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),textvariable=self.var_atten_time)
        atten_time.grid(row=17,column=1,padx=2,pady=10,sticky=W)

        #date
        dateLable=Label(left_inside_frame,text="Date",font=("times new roman",12,"bold"),fg="red")
        dateLable.grid(row=19,column=0,padx=10,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),textvariable=self.var_atten_date)
        atten_date.grid(row=19,column=1,padx=2,pady=10,sticky=W)

        #attendance 
        attendace_Lable=Label(left_inside_frame,text="Attendance Status",font=("times new roman",12,"bold"),fg="red")
        attendace_Lable.grid(row=21,column=0,padx=10,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent",)
        self.atten_status.grid(row=21,column=1,padx=2,pady=10,sticky=W)
        self.atten_status.current(0)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=340,width=490,height=35)
        
        
        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=14,font=("times new roman",14,"bold"),bg="black",fg="orange")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=14,font=("times new roman",14,"bold"),bg="black",fg="orange")
        export_btn.grid(row=0,column=1)

        # update_btn=Button(btn_frame,text="Update",width=12,font=("times new roman",14,"bold"),bg="black",fg="orange")
        # update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",14,"bold"),bg="black",fg="orange")
        reset_btn.grid(row=0,column=2)

        #right label fram
        right_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=690,y=10,width=670,height=680)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=650,height=600)

    #============= scroll Bar table ===========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    
#================== fetch date =================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows :
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","NO DATA TO EXPORT",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")))
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("data export","Your data Exported To " +os.path.basename(fln) +" sSuccesfully !!! ")
        except Exception as es :
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    #get cursor data
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        

    #reset data
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


   


if __name__=="__main__":#for call main
    root=Tk()#calling root with tool kit
    obj=Attendance(root)#pass root in class
    root.mainloop()#creating window      