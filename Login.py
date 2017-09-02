from tkinter import *
from urllib.request import urlopen
import tkinter.messagebox as tm
import os
def Registration():
	def Register():
		URL = urlopen("http://192.241.244.177/ChatApplication/Registration.php?UserId=" + UserId.get() + "&UserName=" + Username.get() + "&Password=" + Password.get()+"")
		for value in URL:
			if int(value.decode()) == 1:
				tm.showinfo("SignIn", "Registration Successful.")
				RegistrationForm.destroy()
			else:
				tm.showerror("SignIn error", "Please try again.")
	def CheckForEmptyFields():
		if Password.get == "" or UserId.get() == "" or Username.get() == "":
			tm.showerror("SignIn error", "Please enter all details.")
		else:
			CheckPasswordMatch()
	def CheckPasswordMatch():
		if Password.get() == ConfirmPassword.get():
			CheckForUniqueUserId()
		else:
			tm.showerror("SignIn error", "Password's doesn't match.")
	def CheckForUniqueUserId():
		URL = urlopen("http://192.241.244.177/ChatApplication/CheckRegistration.php?UserId=" + UserId.get() +"")
		UserIdFound = 0
		for value in URL:
			if int(value.decode()) == 0:
				UserIdFound = UserIdFound + 1 # URL returns 0 if UserId deoesn't exists.
		if UserIdFound == 1:
			Register()
			os.system("python3 Login.py")
		else:
			tm.showerror("SignIn error", "User Id already exists.")
	RegistrationForm = Tk()
	RegistrationForm.title("Registration Form")
	width, height = RegistrationForm.winfo_screenwidth(), RegistrationForm.winfo_screenheight()
	RegistrationForm.geometry('%dx%d+0+0' % (width,height))
	Label(RegistrationForm, text = "User Id").grid(row = 1, column = 1, sticky = W+E+N+S)
	Label(RegistrationForm, text = "User Name").grid(row = 2, column = 1, sticky = W+E+N+S)
	Label(RegistrationForm, text = "Password").grid(row = 3, column=1, sticky = W+E+N+S)
	Label(RegistrationForm, text = "Confirm Password").grid(row = 4, column=1, sticky = W+E+N+S)

	UserId = Entry(RegistrationForm)
	Username = Entry(RegistrationForm)
	Password = Entry(RegistrationForm)
	ConfirmPassword = Entry(RegistrationForm)

	UserId.grid(row = 1, column = 3)
	Username.grid(row = 2, column = 3)
	Password.grid(row = 3, column = 3)
	ConfirmPassword.grid(row = 4, column = 3)
	ButtonState = Button(RegistrationForm, text='Register',state ='normal', command=CheckForEmptyFields).grid(row = 5, column=2)
	mainloop( )
def CheckLogin():
    url = urlopen("http://192.241.244.177/ChatApplication/CheckLogin.php?UserId=" + UserId.get() + "&Password=" + Password.get() +"")
    LoginValue = 0
    for value in url:
        if int(value.decode()) == 1:
            LoginValue = LoginValue + 1
    if LoginValue == 1:
        tm.showinfo("Login ", "Login Successful.")
    else:
        tm.showerror("Login error.", "Login failed.")
LoginForm = Tk()
LoginForm.title("Chat Application")
width, height = LoginForm.winfo_screenwidth(), LoginForm.winfo_screenheight()
LoginForm.geometry('%dx%d+0+0' % (width,height))
Label(LoginForm, text = "Chat Application").grid(row = 2, column = 4)
Label(LoginForm, text = "User Id").grid(row = 4, column = 3)
Label(LoginForm, text = "Password").grid(row = 5, column=3)

UserId = Entry(LoginForm)
Password = Entry(LoginForm)

UserId.grid(row = 4, column = 4)
Password.grid(row = 5, column = 4)

logbtn = Button(LoginForm, text="Login", fg="blue", command = CheckLogin).grid(row = 6, column = 3)
logbtn = Button(LoginForm, text="Register", fg="blue", command = Registration).grid(row = 6, column = 4)
mainloop()