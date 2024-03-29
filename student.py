from tkinter import* #for gui application
from tkinter import ttk#in ttk stylist tool
from PIL import Image,ImageTk#for image crop fix
from tkinter import messagebox#for show message
import mysql.connector

import cv2# for algorithm
import re

class Student:
    def __init__(self,root):#construction call (root =window name(1st self))
        self.root=root#initialize
        self.root.geometry("1080x720+0+0")#(width,height,x start from 0,y start form 0)
        self.root.title("Face Recognition Attendance System")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_stdid=StringVar()
        self.var_stdname=StringVar()
        self.var_div=StringVar()
        self.var_rollno=StringVar()
        self.var_phoneno=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_address=StringVar()
        self.var_teachername=StringVar()
        self.var_subject=StringVar()
    
        #background img
        img3=Image.open(r"imges\stubg.jpg")
        img3=img3.resize((1530,790),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        #title
        title_n=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("sans-serif",35,"bold"),bg="black",fg="yellow")
        title_n.place(x=0,y=0,width=1530,height=70)

        #main frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=90,width=1390,height=750)

        #left label fram
        left_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"),fg="blue")
        left_frame.place(x=10,y=10,width=650,height=680)

        #first image
        img_left=Image.open(r"imges\students.jpg")
        img_left=img_left.resize((510,150),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg=ImageTk.PhotoImage(img_left)
        
        f_lb=Label(left_frame,image=self.photoimg)
        f_lb.place(x=120,y=10,width=400,height=150)


        #current course
        Currentcourse_frame=LabelFrame(left_frame,bd=4,relief=RIDGE,text="Current Course Information",fg="green",font=("times new roman",12,"bold"))
        Currentcourse_frame.place(x=10,y=155,width=620,height=120)

        #department
        dep_label=Label(Currentcourse_frame,text="Department",font=("times new roman",12,"bold"),fg="red")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_comb=ttk.Combobox(Currentcourse_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_comb["values"]=("Select Department","Computer Science","Physics","Chemistry","Maths")
        dep_comb.current(0)
        dep_comb.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        cou_label=Label(Currentcourse_frame,text="Course",font=("times new roman",12,"bold"),fg="red")
        cou_label.grid(row=0,column=2,padx=10,sticky=W)

        cou_comb=ttk.Combobox(Currentcourse_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        cou_comb["values"]=("Select Course","FY","SY","TY","M-FY","M-SY")
        cou_comb.current(0)
        cou_comb.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        yea_label=Label(Currentcourse_frame,text="Year",font=("times new roman",12,"bold"),fg="red")
        yea_label.grid(row=1,column=0,padx=10,sticky=W)

        yea_comb=ttk.Combobox(Currentcourse_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        yea_comb["values"]=("Select Year","2020","2021","2022")
        yea_comb.current(0)
        yea_comb.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #sem
        sem_label=Label(Currentcourse_frame,text="Semiter",font=("times new roman",12,"bold"),fg="red")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_comb=ttk.Combobox(Currentcourse_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_comb["values"]=("Select Semister","1st","2nd","3rd","4th","5th","6th")
        sem_comb.current(0)
        sem_comb.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class studentcourse
        Classstu_frame=LabelFrame(left_frame,bd=4,relief=RIDGE,text="Class Student Information",fg="green",font=("times new roman",12,"bold"))
        Classstu_frame.place(x=10,y=275,width=620,height=370)

        #student id
        stuid_label=Label(Classstu_frame,text="StudentID",font=("times new roman",12,"bold"),fg="red")
        stuid_label.grid(row=0,column=0,padx=10,sticky=W)

        stuid_entry=ttk.Entry(Classstu_frame,textvariable=self.var_stdid,width=20,font=("times new roman",12,"bold"))
        stuid_entry.grid(row=0,column=1,pady=10,padx=2,sticky=W)

        #student name
        stuname_label=Label(Classstu_frame,text="Student Name",font=("times new roman",12,"bold"),fg="red")
        stuname_label.grid(row=1,column=0,padx=10,sticky=W)

        stuname_entry=ttk.Entry(Classstu_frame,textvariable=self.var_stdname,width=20,font=("times new roman",12,"bold"))
        stuname_entry.grid(row=1,column=1,pady=10,padx=2,sticky=W)

        #class division
        div_label=Label(Classstu_frame,text="Class Divison",font=("times new roman",12,"bold"),fg="red")
        div_label.grid(row=0,column=2,padx=10,sticky=W)

        div_comb=ttk.Combobox(Classstu_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=17,state="readonly")
        div_comb["values"]=("Select Divison","A","B","C","D")
        div_comb.current(0)
        div_comb.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #roll no
        roll_label=Label(Classstu_frame,text="Roll NO",font=("times new roman",12,"bold"),fg="red")
        roll_label.grid(row=1,column=2,padx=10,sticky=W)

        roll_entry=ttk.Entry(Classstu_frame,textvariable=self.var_rollno,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Gender
        gen_label=Label(Classstu_frame,text="Gender",font=("times new roman",12,"bold"),fg="red")
        gen_label.grid(row=2,column=0,padx=10,sticky=W)

        gen_comb=ttk.Combobox(Classstu_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        gen_comb["values"]=("Select Gender","Male","Female")
        gen_comb.current(0)
        gen_comb.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #phone no
        phone_label=Label(Classstu_frame,text="Phone NO",font=("times new roman",12,"bold"),fg="red")
        phone_label.grid(row=2,column=2,padx=10,sticky=W)

        phone_entry=ttk.Entry(Classstu_frame,textvariable=self.var_phoneno,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        #email
        mail_label=Label(Classstu_frame,text="Email",font=("times new roman",12,"bold"),fg="red")
        mail_label.grid(row=3,column=0,padx=10,sticky=W)

        mail_entry=ttk.Entry(Classstu_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        mail_entry.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        #address
        add_label=Label(Classstu_frame,text="Address",font=("times new roman",12,"bold"),fg="red")
        add_label.grid(row=3,column=2,padx=10,sticky=W)

        add_entry=ttk.Entry(Classstu_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        add_entry.grid(row=3,column=3,padx=2,pady=10,sticky=W)

        #teacer name
        tea_label=Label(Classstu_frame,text="Teacher Name",font=("times new roman",12,"bold"),fg="red")
        tea_label.grid(row=4,column=0,padx=10,sticky=W)

        tea_entry=ttk.Entry(Classstu_frame,textvariable=self.var_teachername,width=20,font=("times new roman",12,"bold"))
        tea_entry.grid(row=4,column=1,padx=2,pady=10,sticky=W)

        #subject name
        sub_label=Label(Classstu_frame,text="Subject",font=("times new roman",12,"bold"),fg="red")
        sub_label.grid(row=4,column=2,padx=10,sticky=W)

        sub_entry=ttk.Entry(Classstu_frame,textvariable=self.var_subject,width=20,font=("times new roman",12,"bold"))
        sub_entry.grid(row=4,column=3,padx=2,pady=10,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radio1=ttk.Radiobutton(Classstu_frame,variable=self.var_radio1,text="Take Photo Sampple",value="Yes")
        radio1.grid(row=6,column=0)

        radio2=ttk.Radiobutton(Classstu_frame,variable=self.var_radio1,text="No Photo Sampple",value="No")
        radio2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(Classstu_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=260,width=560,height=35)
        
        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=12,font=("times new roman",14,"bold"),bg="black",fg="orange")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,width=12,font=("times new roman",14,"bold"),bg="black",fg="orange")
        update_btn.grid(row=0,column=1)

        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=12,font=("times new roman",14,"bold"),bg="black",fg="orange")
        reset_btn.grid(row=0,column=2)

        delete_btn=Button(btn_frame,text="DELETE",command=self.del_data,width=12,font=("times new roman",14,"bold"),bg="black",fg="orange")
        delete_btn.grid(row=0,column=3)

        #button frame
        btn_frame1=Frame(Classstu_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=300,width=560,height=35)

        take_btn=Button(btn_frame1,text="TAKE PHOTO SAMPLE",command=self.generate_dataset,width=25,font=("times new roman",14,"bold"),bg="black",fg="orange")
        take_btn.grid(row=0,column=0)

        up_btn=Button(btn_frame1,text="UPDATE PHOTO SAMPLE",width=25,font=("times new roman",14,"bold"),bg="black",fg="orange")
        up_btn.grid(row=0,column=2)

        #right label fram
        right_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=690,y=10,width=670,height=680)

        #first image
        img_right=Image.open(r"imges\attendance.jpg")
        img_right=img_right.resize((510,150),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg1=ImageTk.PhotoImage(img_right)
        
        f_lb1=Label(right_frame,image=self.photoimg1)
        f_lb1.place(x=120,y=10,width=400,height=150)

        #search system
        Search_frame=LabelFrame(right_frame,bd=4,relief=RIDGE,text="Search System",fg="green",font=("times new roman",12,"bold"))
        Search_frame.place(x=10,y=155,width=620,height=120)

        #search by
        sea_label=Label(Search_frame,text="Search By",font=("times new roman",12,"bold"),fg="red")
        sea_label.grid(row=0,column=0,padx=10,sticky=W)

        sea_comb=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        sea_comb["values"]=("Select ","Roll NO","Phone No")
        sea_comb.current(0)
        sea_comb.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #search entry
        sea_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        sea_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #buttons
        sea_btn=Button(Search_frame,text="SEARCH",width=12,font=("times new roman",12,"bold"),bg="black",fg="orange")
        sea_btn.grid(row=1,column=1)

        show_btn=Button(Search_frame,text="SHOW ALL",width=12,font=("times new roman",12,"bold"),bg="black",fg="orange")
        show_btn.grid(row=1,column=3,padx=5)

        #table frame
        table_frame=LabelFrame(right_frame,bd=4,relief=RIDGE)
        table_frame.place(x=10,y=276,width=620,height=370)

        #sroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("department","course","year","semister","id","div","name","rollno","gender","phoneno","email","address","teachername","subject","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("department",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semister",text="Semister")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("div",text="Class Division")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("rollno",text="Roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phoneno",text="Phone No")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teachername",text="TeacherName")
        self.student_table.heading("subject",text="Subject")
        self.student_table.heading("photo",text="Photosamplestatus")
        self.student_table["show"]="headings"

        self.student_table.column("department",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semister",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("phoneno",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teachername",width=100)
        self.student_table.column("subject",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # #checkphoneno
    # def checkphone(self,contact):
    #     if contact.isdigit():
    #         return True
    #     if len(str(contact)==0)  
    # 
    #check emmail
    def checkemail(self,email) :
        if len(email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else:
                messagebox.showerror("Error","invalid email",parent=self.root) 
                return False
        else:
            messagebox.showerror("Error","Email length too small")           



    #function declation
    def add_data(self):    
        if self.var_dep.get()=="Select Department" or self.var_stdname.get()=="" or self.var_stdid.get()==""or self.var_address.get()=="" or self.var_course.get()=="" or self.var_div.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_phoneno.get()=="" or self.var_radio1.get()=="" or self.var_sem.get()=="" or self.var_rollno.get()=="" or self.var_subject.get()=="" or self.var_teachername.get()=="" or self.var_year.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

            if len(self.var_phoneno.get())!=10:
                messagebox.showerror("Error","invalid phone no",parent=self.root)

                if self.var_email.get()!=None:
                    x=self.checkemail(self.var_email.get())    
        
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition_db")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_stdid.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_stdname.get(),
                                                                                                                self.var_rollno.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_phoneno.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teachername.get(),
                                                                                                                self.var_subject.get(),
                                                                                                                self.var_radio1.get()
                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student detials added successfully",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)   

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition_db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()        

    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_stdid.set(data[4]),
        self.var_div.set(data[5]),
        self.var_stdname.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_phoneno.set(data[9]),
        self.var_email.set(data[10]),
        self.var_address.set(data[11]),
        self.var_teachername.set(data[12]),
        self.var_subject.set(data[13]),
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stdname.get=="" or self.var_stdid.get=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Deatils",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition_db")
                    my_cursor=conn.cursor() 
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semister=%s, Divison=%s,StudentName=%s,Rollno=%s,Gender=%s,Phoneno=%s,Email=%s,Address=%s,Teachername=%s,Subject=%s,Photosample=%s where StudentID=%s",(

                                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                                self.var_stdname.get(),
                                                                                                                                                                                                                                self.var_rollno.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_phoneno.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_teachername.get(),
                                                                                                                                                                                                                                self.var_subject.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                self.var_stdid.get()
                                                                                                                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root) 
                conn.commit()
                self.fetch_data()
                conn.close()       
            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)

    #delete function   
    def del_data(self):
        if self.var_stdid.get()=="":
            messagebox.showerror("Error","Student id must required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition_db")
                    my_cursor=conn.cursor() 
                    sql="delete from student where StudentID=%s"
                    val=(self.var_stdid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete Student",parent=self.root)             
            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)

    #reset 
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semister")
        self.var_stdid.set("")
        self.var_div.set("Select Divison")
        self.var_stdname.set("")
        self.var_rollno.set("")
        self.var_gender.set("Select Gender")
        self.var_phoneno.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_teachername.set("")
        self.var_subject.set("")
        self.var_radio1.set("")

    #genearte data sets and samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stdname.get=="" or self.var_stdid.get=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition_db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1 
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semister=%s, Divison=%s,StudentName=%s,Rollno=%s,Gender=%s,Phoneno=%s,Email=%s,Address=%s,Teachername=%s,Subject=%s,Photosample=%s where StudentID=%s",(

                                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                                self.var_stdname.get(),
                                                                                                                                                                                                                                self.var_rollno.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_phoneno.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_teachername.get(),
                                                                                                                                                                                                                                self.var_subject.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                self.var_stdid.get()==id+1
                                                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 

            #load predifiend data on face file form cv2
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    # minimum neibhor=5


                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                #camera open
                cap=cv2.VideoCapture(0)#0 for web camera
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))#crop
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg" 
                        cv2.imwrite(file_name_path,face)  
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")
            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)
   
if __name__=="__main__":#for call main
    root=Tk()#calling root with tool kit
    obj=Student(root)#pass root in class
    root.mainloop()#creating window                                                                                                                                                                                                                               
                                                                  

                    
                                                                                                                                                

                                                                                                                                                    
