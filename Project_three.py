from tkinter import *
from tkinter.font import Font
import mysql.connector

root=Tk()
myfont = Font(family="Arial Unicode Ms", size=10, weight="bold")
root.title("Application Form")
root.geometry("500x700")
root.resizable(False, False)


def mydetails():

    mydb = mysql.connector.connect(host="localhost", username="root", password='', database="thangam")
    curs = mydb.cursor()
    sql = "insert into user_details(Name,Age,Gender,Mobile_Number,Parent_or_Guardian,College_Name,Department,Semester,Year_of_Study,Educational_Year) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);  "
    values = [[name.get(),age.get(),options.get(),mobileNumber.get(),parentorgaurdian.get(),collgename.get(),department.get(),sem.get(),year.get(),ed_year.get()]]
    curs.executemany(sql, values)
    print(values)
    mydb.commit()

header_lbl = Label(root, text="STUDENT INFO", fg='black', font=("Arial", 14, "bold")).grid(row=0, column=1,padx=5, pady=10)
name = StringVar()
name_lbl = Label(root, text="Name", fg='black',font=myfont).grid(row=3, column=0, padx=10)
name_entry = Entry(root, textvariable=name, fg="blue",font=myfont, bd=2, ).grid(row=3, column=1, ipadx=40, ipady=2, padx=10,pady=5)

age = StringVar()
age_lbl = Label(root, text="Age", fg='black',font=myfont).grid(row=4, column=0, padx=10)
age_entry = Entry(root, textvariable=age, fg="blue",font=myfont, bd=2, ).grid(row=4, column=1, ipadx=40, ipady=2, padx=10,pady=5)

genderopt = ["Male", "Female"]
options = StringVar()
options.set("Gender")
gender_lbl = Label(root, text="Gender", fg='black',font=myfont).grid(row=5, column=0, padx=10)
gender_option = OptionMenu(root, options, *genderopt).grid(row=5, column=1, ipadx=65, ipady=2, padx=10, pady=5)

mobileNumber = IntVar()
mobile_no_lbl = Label(root, text="Mobile Number", fg='black',font=myfont).grid(row=6, column=0, padx=10)
mobile_no_entry = Entry(root, textvariable=mobileNumber, fg="blue",font=myfont, bd=2, ).grid(row=6, column=1, ipadx=40,ipady=2, padx=10, pady=5)

parentorgaurdian = StringVar()
p_g_lbl = Label(root, text="Parent/Gaurdian Name", fg='black',font=myfont).grid(row=7, column=0, padx=10)
p_g_entry = Entry(root, textvariable=parentorgaurdian, fg="blue",font=myfont, bd=2, ).grid(row=7, column=1, ipadx=40, ipady=2,padx=10, pady=5)

separator_lbl = Label(root,text="-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-",fg='black').grid(row=9, pady=20, columnspan=10)

Education_lbl = Label(root, text=" EDUCATIONAL INFO", fg='black', font=("Arial", 14, "bold")).grid(row=10,column=1)

collgename = StringVar()
college_lbl = Label(root, text="College Name", fg='black',font=myfont).grid(row=11, column=0, padx=10)
college_entry = Entry(root, textvariable=collgename, fg="blue",font=myfont, bd=2, ).grid(row=11, column=1, ipadx=40, ipady=2,padx=10,pady=5)

department = StringVar()
department_lbl = Label(root, text="Department", fg='black',font=myfont).grid(row=12, column=0, padx=10)
department_entry = Entry(root, textvariable=department, fg="blue",font=myfont, bd=2, ).grid(row=12, column=1, ipadx=40,ipady=2, padx=10, pady=5)

semopt = ['1', '2', '3', '4', '5', '6', '7', '8']
sem = StringVar()
sem.set("Current Semester")
sem_lbl = Label(root, text="Current Semester", fg='black',font=myfont).grid(row=13, column=0, padx=10)
sem_entry = OptionMenu(root, sem, *semopt).grid(row=13, column=1, ipadx=40, ipady=2, padx=10,pady=5)

year = StringVar()
year_lbl = Label(root, text="Current Year", fg='black',font=myfont).grid(row=14, column=0, padx=10)
year_entry = Entry(root, textvariable=year, fg="blue",font=myfont, bd=2, ).grid(row=14, column=1, ipadx=40, ipady=2, padx=10,pady=5)

ed_year = StringVar()
ed_year_lbl = Label(root, text="Educational Year", fg='black',font=myfont).grid(row=15, column=0, padx=10)
ed_year_entry = Entry(root, textvariable=ed_year, fg="blue",font=myfont, bd=2, ).grid(row=15, column=1, ipadx=40, ipady=2,padx=10,pady=5)

update_btn = Button(root, text="Update", fg="white",font=myfont, bg="blue", command=mydetails).grid(row=16, column=1, columnspan=2,ipadx=10, ipady=2)


root.mainloop()