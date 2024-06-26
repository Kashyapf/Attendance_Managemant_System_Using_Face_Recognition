from tkinter import *
from tkinter import ttk #We import ttk for beautiful and useful toolkit
from PIL import Image,ImageTk #importing image editing,croping and working with image in Gui.
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition

#creating class of face recognition system.
class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        #Image 1
        img = Image.open(r"college_images\Stanford.jpg")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_label1 = Label(self.root,image=self.photoimg)
        f_label1.place(x=0,y=0,width=500,height=130)

        #Image 2
        img1 = Image.open(r"college_images\facialrecognition.png")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_label1 = Label(self.root,image=self.photoimg1)
        f_label1.place(x=500,y=0,width=500,height=130)

        #Image 3
        img2 = Image.open(r"college_images\university.jpg")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_label1 = Label(self.root,image=self.photoimg2)
        f_label1.place(x=1000,y=0,width=500,height=130)
        
        #Background Image
        bg = Image.open(r"college_images\wp2551980.jpg")
        bg.resize((1366,768),Image.ANTIALIAS)
        self.bgphoto = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root,image=self.bgphoto)
        bg_img.place(x=0,y=130,width=1366,height=768)

        #Creating Title of GUI
        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        #Student Button
        img3 = Image.open(r"college_images\gettyimages-1022573162.jpg")
        img3 = img3.resize((200, 200), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img,image=self.photoimg3,command=self.student_details,cursor="hand2",highlightthickness=1)
        b1.place(x=100,y=60,width=200,height=200)

        b1_1 = Button(bg_img,text="Student Details",cursor="hand2",command=self.student_details,font=("times new roman",15,"bold"),bg="dark blue",fg="white",highlightthickness=1)
        b1_1.place(x=100,y=260,width=200,height=40)

        #Face Detection Button
        img4 = Image.open(r"college_images\face_detector1.jpg")
        img4 = img4.resize((200, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.face_data,highlightthickness=1)
        b1.place(x=400, y=60, width=200, height=200)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white", highlightthickness=1)
        b1_1.place(x=400, y=260, width=200, height=40)

        #Attendance Face Button
        img5 = Image.open(r"college_images\smart-attendance.jpg")
        img5 = img5.resize((200, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", highlightthickness=1)
        b1.place(x=700, y=60, width=200, height=200)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white", highlightthickness=1)
        b1_1.place(x=700, y=260, width=200, height=40)

        #Help desk
        img6 = Image.open(r"college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img6 = img6.resize((200, 200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", highlightthickness=1)
        b1.place(x=1000, y=60, width=200, height=200)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white", highlightthickness=1)
        b1_1.place(x=1000, y=260, width=200, height=40)

        #Train Face button
        img7 = Image.open(r"college_images\facialrecognition1.png")
        img7 = img7.resize((200, 200), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.train_data)
        b1.place(x=100, y=310, width=200, height=200)

        b1_1 = Button(bg_img, text="Train Face", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white", highlightthickness=1)
        b1_1.place(x=100, y=510, width=200, height=40)

        # Photos face  button
        img8 = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img8 = img8.resize((200, 200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.open_img,)
        b1.place(x=400, y=310, width=200, height=200)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white", highlightthickness=1)
        b1_1.place(x=400, y=510, width=200, height=40)

        #Developers  button
        img9 = Image.open(r"college_images\Team-Management-Software-Development.jpg")
        img9 = img9.resize((200, 200), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", highlightthickness=1)
        b1.place(x=700, y=310, width=200, height=200)

        b1_1 = Button(bg_img, text="Developers", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white", highlightthickness=1)
        b1_1.place(x=700, y=510, width=200, height=40)

        # Exit face  button
        img10 = Image.open(r"college_images\exit.jpg")
        img10 = img10.resize((200, 200), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", highlightthickness=1)
        b1.place(x=1000, y=310, width=200, height=200)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white", highlightthickness=1)
        b1_1.place(x=1000, y=510, width=200, height=40)


    def open_img(self):
        os.startfile("data")

    #=========================================Function button==============================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        
        self.app = Train(self.new_window)    

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)            


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()


def sample_function():
    pass



