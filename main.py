from cProfile import label
from cgitb import text
from tkinter import* #for gui application
from tkinter import ttk#in ttk stylist tool
from PIL import Image,ImageTk#for image crop fix
from student import Student

from train import Train
import os
from train import Train
import cv2
from face_recognition import Face_Recognition
from attendance import Attendance
import tkinter
from time import strftime
from datetime import datetime



class Face_Recognition_System:
    def __init__(self,root):#construction call (root =window name(1st self))
        self.root=root#initialize
        self.root.geometry("1080x720+0+0")#(width,height,x start from 0,y start form 0)
        self.root.title("Face Recognition Attendance System")

        #first image
        img=Image.open(r"imges\fc2.jpg")
        img=img.resize((510,150),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb=Label(self.root,image=self.photoimg)
        f_lb.place(x=0,y=0,width=510,height=150)

        #second img
        img1=Image.open(r"imges\middle.jpg")
        img1=img1.resize((510,150),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb=Label(self.root,image=self.photoimg1)
        f_lb.place(x=510,y=0,width=510,height=150)

         #third img
        img2=Image.open(r"imges\fc2.jpg")
        img2=img2.resize((510,150),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb=Label(self.root,image=self.photoimg2)
        f_lb.place(x=1020,y=0,width=500,height=150)

        #background img
        img3=Image.open(r"imges\bg1.jpg")
        img3=img3.resize((1530,790),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1530,height=790)
        
        #title
        title_n=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM",font=("sans-serif",35,"bold"),fg="red")
        title_n.place(x=0,y=0,width=1530,height=70)

        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lb1.config(text=string)
            lb1.after(1000,time)

        lb1=Label(title_n,font=('times new roman',14,'bold'),background='white',foreground='blue') 
        lb1.place(x=0,y=0,width=110,height=50)
        time()   

        #student info button
        img4=Image.open(r"imges\student.jfif")
        img4=img4.resize((200,170),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_detail,cursor="hand2")
        b1.place(x=450,y=100,width=200,height=170)

        b1_n=Button(bg_img,text="Student Details",command=self.student_detail,cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="yellow")
        b1_n.place(x=450,y=270,width=200,height=30)


        #detect face button
        img5=Image.open(r"imges\face.jfif")
        img5=img5.resize((200,170),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=850,y=100,width=200,height=170)

        b2_n=Button(bg_img,text="Face Detection",cursor="hand2",command=self.face_data,font=("times new roman",20,"bold"),bg="black",fg="yellow")
        b2_n.place(x=850,y=270,width=200,height=30)

        
        #attendance
        img6=Image.open(r"imges\attendance.jpg")
        img6=img6.resize((200,170),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=1250,y=100,width=200,height=170)

        b3_n=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",20,"bold"),bg="black",fg="yellow")
        b3_n.place(x=1250,y=270,width=200,height=30)

        #train data
        img7=Image.open(r"imges\train.jpg")
        img7=img7.resize((200,170),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,command=self.train_data,cursor="hand2")
        b4.place(x=450,y=380,width=200,height=170)

        b4_n=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="yellow")
        b4_n.place(x=450,y=540,width=200,height=30)

        #photos
        img8=Image.open(r"imges\photos.jpg")
        img8=img8.resize((200,170),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b5.place(x=850,y=380,width=200,height=170)

        b5_n=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",20,"bold"),bg="black",fg="yellow")
        b5_n.place(x=850,y=540,width=200,height=30)

        #exit button
        img9=Image.open(r"imges\exit.png")
        img9=img9.resize((200,170),Image.LANCZOS)#width height,convert high levelimage to low level
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.exit)
        b6.place(x=1250,y=380,width=200,height=170)

        b6_n=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",20,"bold"),bg="black",fg="yellow")
        b6_n.place(x=1250,y=540,width=200,height=30)


    def open_img(self):
        os.startfile("data")    

    #function button
    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)   

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are u sure to exit project",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return        


        


if __name__=="__main__":#for call main
    root=Tk()#calling root with tool kit
    obj=Face_Recognition_System(root)#pass root in class
    root.mainloop()#creating window 
        
