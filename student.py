from tkinter import *
from tkinter import ttk #We import ttk for beautiful and useful toolkit
from PIL import Image,ImageTk #importing image editing,croping and working with image in Gui.
from tkinter import messagebox
import mysql.connector
import cv2

# from roughfile import detect_faces



class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Details")

        #===================================variable===================================
        self.var_dep=StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_mentor = StringVar()


        #Image 1
        img = Image.open(r"C:\Users\Client\Desktop\MINI PROJECT\college_images\face-recognition.png")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_label1 = Label(self.root,image=self.photoimg)
        f_label1.place(x=0,y=0,width=500,height=130)

        #Image 2
        img1 = Image.open(r"C:\Users\Client\Desktop\MINI PROJECT\college_images\imgref3_orig.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_label1 = Label(self.root,image=self.photoimg1)
        f_label1.place(x=500,y=0,width=500,height=130)

        #Image 3
        img2 = Image.open(r"C:\Users\Client\Desktop\MINI PROJECT\college_images\facial-recognition_0.jpg")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_label1 = Label(self.root,image=self.photoimg2)
        f_label1.place(x=1000,y=0,width=500,height=130)

        # Background Image
        bg = Image.open(r"C:\Users\Client\Desktop\MINI PROJECT\college_images\wp2551980.jpg")
        bg.resize((1366, 768), Image.ANTIALIAS)
        self.bgphoto = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image=self.bgphoto)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Creating Title of GUI
        title_lbl = Label(bg_img, text="Student Details",
                          font=("times new roman", 35, "bold"), bg="white", fg="green",background="yellow")
        title_lbl.place(x=0, y=0, width=1366, height=50)

        #Creating Frame
        main_frame = Frame(bg_img,bd=2,background="white")
        main_frame.place(x=0,y=50,width=1366,height=700)

        ##Left side label frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),background="white")
        Left_frame.place(x=5,y=5,width=660,height=490)

        img_left = Image.open(r"C:\Users\Client\Desktop\MINI PROJECT\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((700, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_label1 = Label(Left_frame, image=self.photoimg_left)
        f_label1.place(x=0, y=0, width=660, height=130)

        ###Current Course
        Current_course_frame= LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Course Information",font=("times new roman", 12, "bold"), background="white")
        Current_course_frame.place(x=5, y=130, width=650, height=110)

        ###Department
        dep_label = Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"),background="white")
        dep_label.grid(row=0,column=0,padx=2)

        dep_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        ###Course
        course_label = Label(Current_course_frame, text="Course", font=("times new roman", 12, "bold"),
                          background="white")
        course_label.grid(row=0, column=2, padx=5,sticky=W)

        course_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), width=20, state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)

        ###Year
        year_label = Label(Current_course_frame, text="Year", font=("times new roman", 12, "bold"),
                           background="white")
        year_label.grid(row=1, column=0, padx=5,sticky=W)

        year_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), width=20,
                                  state="readonly")
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10,sticky=W)

        ###Semester
        semester_label = Label(Current_course_frame, text="Semester", font=("times new roman", 12, "bold"),
                           background="white")
        semester_label.grid(row=1, column=2, padx=2,sticky=W)

        semester_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_semester
        ,font=("times new roman", 12, "bold"), width=20,
                                  state="readonly")
        semester_combo["values"] = ("Select Semester", "Semester 1", "Semester 2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2,pady=10,sticky=W)

        ##Class Student Information
        Class_Student_frame= LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Class Student Information",font=("times new roman", 12, "bold"), background="white")
        Class_Student_frame.place(x=5, y=242, width=650, height=220)

        ###Entry-Student ID
        Student_ID_label = Label(Class_Student_frame, text="Student ID:", font=("times new roman", 8, "bold"),
                               background="white")
        Student_ID_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        student_ID_entry = ttk.Entry(Class_Student_frame, width=30, textvariable=self.var_std_id, font=("times new roman", 8, "bold"))
        student_ID_entry.grid(row=0,column=1,padx=5,sticky=W)

        ###Entry-Student Name
        Student_name_label = Label(Class_Student_frame, text="Student Name:", font=("times new roman", 8, "bold"),
                                 background="white")
        Student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_name_entry = ttk.Entry(Class_Student_frame, width=30,textvariable=self.var_std_name, font=("times new roman", 8, "bold"))
        student_name_entry.grid(row=0, column=3, padx=5, sticky=W)

        ###Entry-Student Class Divison
        Class_Div_label = Label(Class_Student_frame, text="Divison:", font=("times new roman", 8, "bold"),
                                 background="white")
        Class_Div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        div_combo = ttk.Combobox(Class_Student_frame, textvariable=self.var_div,
                                   font=("times new roman", 8, "bold"), width=20,
                                   state="readonly")
        div_combo["values"] = ("Select Divison","3","4","5","6","9","11","13")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        ###Entry-Student Roll No
        Roll_No_label = Label(Class_Student_frame, text="Roll No:", font=("times new roman", 8, "bold"),
                                background="white")
        Roll_No_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        Roll_No_entry = ttk.Entry(Class_Student_frame, width=30, textvariable=self.var_roll,font=("times new roman", 8, "bold"))
        Roll_No_entry.grid(row=1, column=3, padx=5, sticky=W)

        ###Entry-Student Gender
        Gender_label = Label(Class_Student_frame, text="Gender:", font=("times new roman", 8, "bold"),
                                background="white")
        Gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(Class_Student_frame, textvariable=self.var_gender,
                                  font=("times new roman", 8, "bold"), width=20,
                                  state="readonly")
        gender_combo["values"] = ("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=5, sticky=W)

        ###Entry-Student DOB
        DOB_label = Label(Class_Student_frame, text="DOB:", font=("times new roman", 8, "bold"),
                          background="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        DOB_entry = ttk.Entry(Class_Student_frame, width=30, textvariable=self.var_dob,font=("times new roman", 8, "bold"))
        DOB_entry.grid(row=2, column=3, padx=5, sticky=W)

        ###Entry-Student Email Id
        Email_label = Label(Class_Student_frame, text="Email ID:", font=("times new roman", 8, "bold"),
                            background="white")
        Email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Email_entry = ttk.Entry(Class_Student_frame, width=30,textvariable=self.var_email, font=("times new roman", 8, "bold"))
        Email_entry.grid(row=3, column=1, padx=5, sticky=W)

        ###Entry-Student Phone No
        Phone_label = Label(Class_Student_frame, text="Phone Number:", font=("times new roman", 8, "bold"),
                             background="white")
        Phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        Phone_entry = ttk.Entry(Class_Student_frame, width=30,textvariable=self.var_phone, font=("times new roman", 8, "bold"))
        Phone_entry.grid(row=3, column=3, padx=5, sticky=W)

        ###Entry-Student Address
        Address_label = Label(Class_Student_frame, text="Address:", font=("times new roman", 8, "bold"),
                            background="white")
        Address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        Address_entry = ttk.Entry(Class_Student_frame, width=30, textvariable=self.var_address,font=("times new roman", 8, "bold"))
        Address_entry.grid(row=4, column=1, padx=5, sticky=W)

        ###Entry-Student Mentor Name
        Mentor_label = Label(Class_Student_frame, text="Mentor Name:", font=("times new roman", 8, "bold"),
                            background="white")
        Mentor_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        Mentor_entry = ttk.Entry(Class_Student_frame, width=30,textvariable=self.var_mentor, font=("times new roman", 8, "bold"))
        Mentor_entry.grid(row=4, column=3, padx=5, sticky=W)





        ##Radio Buttons
        self.var_radio1 = StringVar()
        radio_b1 = ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio_b1.grid(row=5,column=0)

        radio_b2 = ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio_b2.grid(row=5,column=1)

        ##Button Frame
        button_frame = LabelFrame(Class_Student_frame, bd=2, background="white",relief=RIDGE)
        button_frame.place(x=0,y=162,width=645,height=32)

        ### Save button
        save_btn = Button(button_frame,width=9,text="Save",command=self.add_data,font=("times new roman",13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        ### Update button
        update_btn = Button(button_frame, width=9, text="Update",command=self.update_data, font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
        update_btn.grid(row=0, column=1)

        ### Delete button
        delete_btn = Button(button_frame, width=9, text="Delete",command=self.delete_data, font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
        delete_btn.grid(row=0, column=2)

        ### Reset button
        reset_btn = Button(button_frame, width=9, text="Reset",command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
        reset_btn.grid(row=0, column=3)

        ### Take Photo button
        take_btn = Button(button_frame, width=11, command = self.generate_dataset,text="Take Photo", font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
        take_btn.grid(row=0, column=4)

        ### Update Photo button
        update_phto_btn = Button(button_frame, width=12, text="Update Photo", font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
        update_phto_btn.grid(row=0, column=5)





        ##Right side label frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Students Database",font=("times new roman",12,"bold"),background="white")
        Right_frame.place(x=680,y=5,width=660,height=490)

        img_right = Image.open(r"C:\Users\Client\Desktop\MINI PROJECT\college_images\gettyimages-1022573162.jpg")
        img_right = img_right.resize((700, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_label1 = Label(Right_frame, image=self.photoimg_right)
        f_label1.place(x=0, y=0, width=660, height=130)


        #============================================Search System=========================================================
        Search_frame = LabelFrame(Right_frame,text="Search System",bd=2,bg="white",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=130,width=650,height=70)

        ###Search By Label
        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 15, "bold"),
                            background="green",fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        ###Search By Combo Box
        search_combo = ttk.Combobox(Search_frame,font=("times new roman", 15, "bold"),state="readonly",width=10,)
        search_combo["values"]=("Select","Roll No","Phone No","Div","Year","Course")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        ###Show_all_entry
        search_entry = ttk.Entry(Search_frame, width=17, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=5, sticky=W)

        ### Reset by Button
        Show_all_btn = Button(Search_frame, width=9, text="Show All", font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        Show_all_btn.grid(row=0, column=4,padx=5)

        ### Search Button
        search_by_btn = Button(Search_frame, width=9, text="Search", font=("times new roman", 13, "bold"), bg="blue",
                               fg="white")
        search_by_btn.grid(row=0, column=3,padx=5)

        # Table Frame
        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=200,width=650,height=265)

        ##Scroll bar
        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","Id","Name","Div","Roll No","Gender",'DOB','Email',"Phone Number","Address","Mentor Name","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill = X)
        scroll_y.pack(side=RIGHT,fill = Y)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Id",text="Student Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Div")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone Number",text="Phone Number")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Mentor Name",text="Mentor Name")
        self.student_table.heading("Photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone Number",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Mentor Name",width=100)
        self.student_table.column("Photo",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # #====================================function decration =========================================



    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Kldn@19102520",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_mentor.get(),
                                                                                                                self.var_radio1.get()
                                                                                                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", "student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("error", f"due to :{str(es)}", parent=self.root)

#
    # =======fetch data========
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="Kashyap", password="Kldn@19102520",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    # =========get cursor============
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_mentor.set(data[13]),
        self.var_radio1.set(data[14])


    # update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "do you want to update this student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="Kashyap", password="Kldn@19102520",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Divison=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Mentor=%s,PhotoSample=%s where Student_id = %s",(
                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_mentor.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_std_id.get()
                                                                                                                                                                                                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("success,student details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"due to :{str(es)}", parent=self.root)

    # delete function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "studentid must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("student delete page", "do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="Kashyap", password="Kldn@19102520",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("error", f"due to :{str(es)}", parent=self.root)
#
#
    # reset
    def reset_data(self):
        self.var_dep.set("select department"),
        self.var_course.set("select course"),
        self.var_year.set("year"),
        self.var_semester.set("semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("divison"),
        self.var_roll.set(""),
        self.var_gender.set("male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_mentor.set(""),
        self.var_radio1.set("")


    # ======generate data set or take photo samples======#
    def generate_dataset(self):
            if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(host="localhost", username="Kashyap", password="Kldn@19102520",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("SELECT * FROM student")
                    myresult = my_cursor.fetchall()
                    id = 0
                    for x in myresult:
                        id += 1
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Divison=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Mentor=%s,PhotoSample=%s where Student_id = %s",(
                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_mentor.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_std_id.get()==id+1
                                                                                                                                                                                                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()
                    #=================================Load predefined data on face frontals from opencv====================
                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3
                        #Minimum Neighbour = 5

                        for(x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped

                    cap=cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    # cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets completed!!!")
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
                     
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
