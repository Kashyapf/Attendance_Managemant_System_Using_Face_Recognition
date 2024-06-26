from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql. connector
import cv2
import os
import numpy as np
from time import strftime 
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION",font=("times new roman", 35, "bold"), fg="white",bg="black")
        title_lbl.place(x=0, y=0, width=1366, height=55)

        #!st image
        img_top = Image.open(r"college_images\face_detector1.jpg")
        img_top = img_top.resize((555, 635), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_label1 = Label(self.root, image=self.photoimg_top)
        f_label1.place(x=0, y=55, width=555, height=635)

        #2nd image
        img_bottom = Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((950, 635), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_label1 = Label(self.root, image=self.photoimg_bottom)
        f_label1.place(x=555, y=55, width=950, height=635)

        # button
        b1_1 = Button(f_label1,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="black",highlightthickness=1)
        b1_1.place(x=360,y=535,width=220,height=60)

    #============================attendance ============================
    def mark_attendance(self,i,r,d,k):
        with open ("attendance_using_face.csv","r+",newline='\n') as f:
            myDatalist=f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split((","))
                name_list.append(entry[0])
            if (i not in name_list) and (r not in name_list) and (d not in name_list) and (k not in name_list):
                now=datetime.now()
                d1=now.strftime("%D/%M/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{d},{k},{dtString},{d1},Present")
    #   ====================== face recognition==============================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []
            names = []
            roll = []
            Student_id=[]
            Department=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y), (x+w,y+h) ,(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Kldn@19102520",database="face_recognizer")
                my_cursor = conn.cursor()    
                # print("SELECT Name FROM student  WHERE Student_id="+str(id))
                my_cursor.execute("SELECT Name FROM student")
                # print(my_cursor)
                i=my_cursor.fetchall()
                names += i
                
                # print(names)

                my_cursor.execute("SELECT Roll FROM student")
                r=my_cursor.fetchall()
                roll += r
                

                my_cursor.execute("SELECT Department FROM student")
                d=my_cursor.fetchall()
                Department += d                

                my_cursor.execute("SELECT Student_id FROM student")
                k=my_cursor.fetchall()
                Student_id += k

                if confidence>77: 
                    cv2.putText(img,f"ID:{Student_id[0]}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{roll[0]}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{names[0]}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{Department[0]}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,k,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord        

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img  

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")  
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__== "__main__":
    root=Tk()
    obj = Face_Recognition(root)
    root.mainloop()