from tkinter import *
from tkinter import ttk #We import ttk for beautiful and useful toolkit
from PIL import Image,ImageTk #importing image editing,croping and working with image in Gui.
from tkinter import messagebox
import mysql.connector
import cv2

# from roughfile import detect_faces



class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Details")

        #Image 1
        img = Image.open(r"college_images\smart-attendance.jpg")
        img = img.resize((800,150),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_label1 = Label(self.root,image=self.photoimg)
        f_label1.place(x=0,y=0,width=800,height=150)

        #Image 2
        img1 = Image.open(r"college_images\iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((800,150),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)


        f_label1 = Label(self.root,image=self.photoimg1)
        f_label1.place(x=800,y=0,width=800,height=150)

        # Background Image
        bg = Image.open(r"college_images\wp2551980.jpg")
        bg.resize((1366, 768), Image.ANTIALIAS)
        self.bgphoto = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image=self.bgphoto)
        bg_img.place(x=0, y=200, width=1366, height=768)

        #Creating title 
        title_lbl = Label(self.root, text="ATTENDANCE WINDOW",font=("times new roman", 35, "bold"), fg="yellow",bg="indigo")
        title_lbl.place(x=0, y=150, width=1366, height=55)

        #Creating Frame
        main_frame = Frame(root,bd=2,background="white")
        main_frame.place(x=0,y=205,width=1366,height=700)

        ##Left side label frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text=" Student Attendance Details",font=("times new roman",12,"bold"),background="white")
        Left_frame.place(x=5,y=5,width=660,height=470)

        img_left = Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((700, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_label1 = Label(Left_frame, image=self.photoimg_left)
        f_label1.place(x=0, y=0, width=660, height=130)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,background="white")
        left_inside_frame.place(x=0,y=135,width=655,height=310)

        #Labels and Entry
        #Attendance-ID
        Attendance_ID_label = Label(left_inside_frame, text="Attendance Id:", font=("times new roman", 9, "bold"),
                               background="white")
        Attendance_ID_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        Attendance_ID_entry = ttk.Entry(left_inside_frame, width=30, font=("times new roman", 9, "bold"))
        Attendance_ID_entry.grid(row=0,column=1,padx=5,sticky=W)

        #Roll No
        Roll_label = Label(left_inside_frame, text="Roll:", font=("times new roman", 9, "bold"),
                               background="white")
        Roll_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        Roll_entry = ttk.Entry(left_inside_frame, width=30, font=("times new roman", 9, "bold"))
        Roll_entry.grid(row=0,column=3,padx=5,sticky=W)
        

        #Name
        Name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 9, "bold"),
                               background="white")
        Name_label.grid(row=1, column=0, padx=10,pady=5, sticky=W)

        Name_entry = ttk.Entry(left_inside_frame, width=30, font=("times new roman", 9, "bold"))
        Name_entry.grid(row=1,column=1,padx=5,sticky=W)
       
        #Department
        Department_label = Label(left_inside_frame, text="Department:", font=("times new roman", 9, "bold"),
                               background="white")
        Department_label.grid(row=1, column=2, padx=10,pady=5, sticky=W)

        Department_entry = ttk.Entry(left_inside_frame, width=30, font=("times new roman", 9, "bold"))
        Department_entry.grid(row=1,column=3,padx=5,sticky=W)

        #Time
        Time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 9, "bold"),
                               background="white")
        Time_label.grid(row=2, column=0, padx=10,pady=5, sticky=W)

        Time_entry = ttk.Entry(left_inside_frame, width=30, font=("times new roman", 9, "bold"))
        Time_entry.grid(row=2,column=1,padx=5,sticky=W)   
        
        #date
        Date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 9, "bold"),
                               background="white")
        Date_label.grid(row=2, column=2, padx=10,pady=5, sticky=W)

        Date_entry = ttk.Entry(left_inside_frame, width=30, font=("times new roman", 9, "bold"))
        Date_entry.grid(row=2,column=3,padx=5,sticky=W)          

        #Attendance Status
        Attendance_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 9, "bold"),
                               background="white")
        Attendance_label.grid(row=3, column=0, padx=10,pady=5, sticky=W)

        Attendance_combo = ttk.Combobox(left_inside_frame,
                                   font=("times new roman", 9, "bold"), width=30,
                                   state="readonly")
        Attendance_combo["values"] = ("Select","Present","Absent")
        Attendance_combo.current(0)
        Attendance_combo.grid(row=3, column=1, padx=2, pady=5, sticky=W)

        ##Button Frame
        button_frame = LabelFrame(left_inside_frame, bd=2, background="white",relief=RIDGE)
        button_frame.place(x=0,y=250,width=650,height=32)

        ### Import CSV button
        save_btn = Button(button_frame,width=15,text="Import CSV",font=("times new roman",13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        ### Export CSV button
        update_btn = Button(button_frame, width=15, text="Export CSV", font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
        update_btn.grid(row=0, column=1)

        ### Update button
        delete_btn = Button(button_frame, width=15, text="Update", font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
        delete_btn.grid(row=0, column=2)

        ### Reset button
        reset_btn = Button(button_frame, width=16, text="Reset", font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
        reset_btn.grid(row=0, column=3)                



        ##Right side label frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Database",font=("times new roman",12,"bold"),background="white")
        Right_frame.place(x=680,y=5,width=660,height=470)

        table_frame = LabelFrame(Right_frame, bd=2, background="white",relief=RIDGE)
        table_frame.place(x=3,y=3,width=650,height=440)

        #========================Scroll bar======================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","Roll","Name","Department","Time","Date",'Attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill = X)
        scroll_y.pack(side=RIGHT,fill = Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("Roll",text="Roll")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)





if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()      

