import tkinter
from tkinter import ttk
from tkinter import messagebox
def enter_date():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # User Info
        firstname = firstNameEntry.get()
        lastname = lastNameEntry.get()
        if firstname and lastname:

            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # Course info
            reg_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print(f"First Name: {firstname} Last Name: {lastname}")
            print(f"Title: {title} Age: {age} Nationality: {nationality}")
            print(f"# Courses: {numcourses} # Semesters: {numsemesters} ")
            print(f"Registration status: {reg_status}")
            print("----------------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Error", message="Firstname and Lastname are required")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# User details
userinfoFrame= tkinter.LabelFrame(frame, text="User Information")
userinfoFrame.grid(row=0, column=0, padx=20, pady=10)

firstNameLabel =tkinter.Label(userinfoFrame, text="First Name")
firstNameLabel.grid(row=0, column=0)
lastNameLabel =tkinter.Label(userinfoFrame, text="Last Name")
lastNameLabel.grid(row=0, column=1)


firstNameEntry = tkinter.Entry(userinfoFrame)
lastNameEntry = tkinter.Entry(userinfoFrame)
firstNameEntry.grid(row=1, column=0)
lastNameEntry.grid(row=1, column=1)

title_label = tkinter.Label(userinfoFrame, text="Title")
title_combobox = ttk.Combobox(userinfoFrame, values=["","Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(userinfoFrame, text="Age")
age_spinbox = tkinter.Spinbox(userinfoFrame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(userinfoFrame, text="Nationality")
nationality_combobox = ttk.Combobox(userinfoFrame, values=["Africa", "Asia", "Europe", "North America", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in userinfoFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# saving course
course_frame = tkinter.LabelFrame(frame)
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(course_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(course_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not Registered" )

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(course_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(course_frame, from_=0, to=50)
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(course_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(course_frame, from_=0, to=3)
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted" )
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter Data", command= enter_date)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)



window.mainloop()