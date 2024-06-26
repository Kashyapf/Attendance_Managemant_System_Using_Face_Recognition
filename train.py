from tkinter import *
from tkinter import ttk #We import ttk for beautiful and useful toolkit
from PIL import Image,ImageTk #importing image editing,croping and working with image in Gui.
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET",font=("times new roman", 35, "bold"), bg="white", fg="red",background="yellow")
        title_lbl.place(x=0, y=0, width=1366, height=50)

        img_top = Image.open(r"college_images\facialrecognition.png")
        img_top = img_top.resize((1360, 290), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_label1 = Label(self.root, image=self.photoimg_top)
        f_label1.place(x=0, y=55, width=1360, height=290)

        # button
        b1_1 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="orange",fg="black",highlightthickness=1)
        b1_1.place(x=0,y=320,width=1360,height=80)

        img_bottom = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img_bottom = img_bottom.resize((1360, 290), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_label1 = Label(self.root, image=self.photoimg_bottom)
        f_label1.place(x=0, y=400, width=1360, height=290)

    def train_classifier(self):
        data_dir = ("data")
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img=Image.open(image).convert('L')  #Gray Scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #============== Train the classifier and save =========================    
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()


