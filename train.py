from tkinter import* #for gui application
from tkinter import ttk#in ttk stylist tool
from PIL import Image,ImageTk#for image crop fix
from tkinter import messagebox#for show message
import cv2# for algorithm
import os
import numpy as np


class Train:
    def __init__(self,root):#construction call (root =window name(1st self))
        self.root=root#initialize
        self.root.geometry("1080x720+0+0")#(width,height,x start from 0,y start form 0)
        self.root.title("Face Recognition Attendance System")

        #title
        title_n=Label(self.root,text="TRAIN DATA SET",font=("sans-serif",35,"bold"),bg="black",fg="yellow")
        title_n.place(x=0,y=0,width=1530,height=70)

        img_top=Image.open(r"imges\train2.png")#add image
        img_top=img_top.resize((1530,325),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=70,width=1530,height=325)
        #button
        b1_t=Button(self.root,text="TO TRAIN DATA CLICK HERE !!! ",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="RED",fg="WHITE")
        b1_t.place(x=0,y=390,width=1530,height=50)

        img_bottom=Image.open(r"imges\train.jpg")#add image
        img_bottom=img_bottom.resize((1530,325),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale conversion
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])#accessing images using spliting with '.'

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training data",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #local binary  pattern histogram algorithm
        #image to pixel to threshold to binary to decimal
        #=========== Training Classifier ============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","DataSet Training Completed Successfully ")



if __name__=="__main__":#for call main
    root=Tk()#calling root with tool kit
    obj=Train(root)#pass root in class
    root.mainloop()#creating window         