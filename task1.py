from tkinter import*
from tkinter import messagebox
win = Tk()
win.title("registration form")
win.geometry('600x600')
starting = Label(win,text='ENTER THE BELOW DETAILS',font=25,foreground='black').place(x=70,y=10)
def register_button():
    name=name_info.get()
    age=age_info.get()
    dob=dob_info.get()
    place=place_info.get()
    email=email_info.get()
    password=password_info.get()
    confirm_password=confirm_password_info.get()
    phno=phno_info.get()

    if name=="":
        messagebox.showwarning("Warning","please enter your name")
    elif age=="":
        messagebox.showwarning("Warning","please enter ur age")
    elif dob=="":
        messagebox.showwarning("Warning","please enter your dob")
    elif place=="":
        messagebox.showwarning("warning","please enter ur place")
    elif email=="":
        messagebox.showwarning("warning","please enter ur email")
    elif password=="":
        messagebox.showwarning("warning","please enter ur password")
    elif confirm_password=="":
        messagebox.showerror("Error","this is not matching the password")
    elif phno=="":
        messagebox.showwarning("warning","please enter ur phno")
    else:
        Label(win,text="you have registered successfully",font='30',fg="green").place(x=145,y=500)    
name = Label(win, text = 'name').place(x=30,y=50)
name_info=StringVar()
entry1 = Entry(win,textvariable=name_info).place(x=95,y=50)
age = Label(win, text = 'age').place(x=30,y=90)
age_info=StringVar()
entry2 = Entry(win,textvariable=age_info).place(x=95,y=90)
dob = Label(win, text = 'DOB').place(x=30,y=130)
dob_info=StringVar()
entry3 = Entry(win,textvariable=dob_info).place(x=95,y=130)
place = Label(win, text = 'place').place(x=30,y=170)
place_info=StringVar()
entry4 = Entry(win,textvariable=place_info).place(x=95,y=170) 
email = Label(win, text = 'email').place(x=30,y=210)
email_info=StringVar()
entry5 = Entry(win,textvariable=email_info).place(x=95,y=210)
password = Label(win, text = 'password').place(x=30,y=250)
password_info=StringVar()
entry6 = Entry(win,textvariable=password_info).place(x=95,y=250)
confirm_password = Label(win, text = 'confirm password').place(x=30,y=290)
confirm_password_info=StringVar()
entry7 = Entry(win,textvariable=confirm_password_info).place(x=135,y=290)
phno = Label(win, text = 'phone number').place(x=30,y=340)
phno_info=StringVar()
entry8 = Entry(win,textvariable=phno_info).place(x=125,y=340) 
register_button = Button(win,text = 'register', activebackground='black', activeforeground='blue',command=register_button).place(x=100,y=380)
win.mainloop()
