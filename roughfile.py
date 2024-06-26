# from tkinter import *
# from tkinter import ttk #We import ttk for beautiful and useful toolkit
# from PIL import Image,ImageTk #importing image editing,croping and working with image in Gui.
# from tkinter import messagebox
# import mysql.connector
# import cv2

# # update function
# def update_data(self):
#     if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
#        messagebox.showerror("Error", "All fields are required", parent=self.root)
#     else:
#         try:
#            update = messagebox.askyesno("update", "do you want to update this student details", parent=self.root)
#            if update > 0:
#                 conn = mysql.connector.connect(host="localhost", username="Kashyap", password="Kldn@19102520",database="face_recognizer")
#                 my_cursor = conn.cursor()
#                 my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Divison=%s,Roll No=%s,Gender=%s,DOB=%s,Email=%s,Phone Number=%s,Address=%s,Mentor Name=%s,Photo Sample Status=%s where Student_Id = %s",(
#                                                            self.var_dep.get(),
#                                                            self.var_course.get(),
#                                                            self.var_year.get(),
#                                                            self.var_semester.get(),
#                                                            self.var_std_name.get(),
#                                                            self.var_div.get(),
#                                                            self.var_roll.get(),
#                                                            self.var_gender.get(),
#                                                            self.var_dob.get(),
#                                                            self.var_email.get(),
#                                                            self.var_phone.get(),
#                                                            self.var_address.get(),
#                                                            self.var_mentor.get(),
#                                                            self.var_radio1.get(),
#                                                            self.var_std_id.get()
#                                                           ))
#            else:
#                 if not update:
#                     return
#            messagebox.showinfo("success,student details successfully update completed", parent=self.root)
#            conn.commit()
#            self.fetch_data()
#            conn.close()
#         except Exception as es:
#             messagebox.showerror("error", f"due to :{str(es)}", parent=self.root)


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

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
                    cv2.putText(img,f"ID:{Student_id}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{roll}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{names}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{Department}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
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