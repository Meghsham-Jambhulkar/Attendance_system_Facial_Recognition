from msilib.schema import Feature
from pyexpat import features
from tkinter import* #for gui application
from tkinter import ttk#in ttk stylist tool
from PIL import Image,ImageTk#for image crop fix
from tkinter import messagebox#for show message
import mysql.connector
import cv2# for algorithm
import os
import numpy as np
from time import strftime
from datetime import datetime


#from main import Face_Recognition_System

class Face_Recognition:
    def __init__(self,root):#construction call (root =window name(1st self))
        self.root=root#initialize
        self.root.geometry("1080x720+0+0")#(width,height,x start from 0,y start form 0)
        self.root.title("Face Recognition Attendance System")

        #title
        title_n=Label(self.root,text="FACE RECOGNITION",font=("sans-serif",35,"bold"),bg="black",fg="yellow")
        title_n.place(x=0,y=0,width=1530,height=70)
        #image 1
        img_top=Image.open(r"imges\boy.jpeg")#add image
        img_top=img_top.resize((800,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=800,height=700)
        #image 2
        img_bottom=Image.open(r"imges\girl.jpeg")#add image
        img_bottom=img_bottom.resize((800,700),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=800,y=55,width=800,height=700)

        #button
        b1_t=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",20,"bold"),bg="darkgreen",fg="WHITE")
        b1_t.place(x=0,y=650,width=250,height=60)

        # ===================Attendance ================

    def mark_attendance(Self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f :
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])

            #for not showing attended again and again
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


# ===================Face Recognition ================
    def face_recog(self):
        def draw_boundry(img,classifier ,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))
        
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition_db")
                my_cursor=conn.cursor()
        
                my_cursor.execute("select StudentName from student where StudentID ="+str(id) )
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Rollno from student where StudentID ="+str(id) )
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where StudentID ="+str(id) )
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select StudentID from student where StudentID ="+str(id) )
                i=my_cursor.fetchone()
                i="+".join(i)

        

                if confidence>80:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll No:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name :{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else :
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face:",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord = [x,y,w,h]

            return coord
    
        def recognize (img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        video_cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

            

if __name__=="__main__":#for call main
    root=Tk()#calling root with tool kit
    obj=Face_Recognition(root)#pass root in class
    root.mainloop()#creating window  