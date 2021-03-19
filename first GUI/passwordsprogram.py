from tkinter import *

class App (Frame):
    usernames = ["Jaxon"]
    password = ["Class1"]
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.trys = 0
        self.create_widgets()

    def create_widgets(self):
        self.lbl1 = Label(self, text = "Welcome to my password program")
        self.lbl2 = Label(self, text = "Username")
        self.lbl3 = Label(self, text = "Password")
        self.button = Button(self, text = "submit")
        self.button["command"] = self.submit
        self.user_tb = Entry(self)
        self.pw_tb2 = Entry(self)
        self.output = Text(self)
        self.output.config(width = 38, height = 3)
        self.hbutton = Button(self, text = "show password")
        self.hbutton ["command"] = self.submit




        self.lbl1.grid(row=0, column=0, columnspan = 2)
        self.lbl2.grid(row=1, column=0,sticky = NW)
        self.lbl3.grid(row=2, column=0,sticky = SW)
        self.button.grid(row=3, column=0,sticky = W)
        self.user_tb.grid(row=1,column=1,columnspan = 2)
        self.pw_tb2.grid(row=2,column=1,columnspan = 2)
        self.pw_tb2.config(show="*")
        self.output.grid(row = 4, column = 0, columnspan = 3)
        self.hbutton.grid(row = 2, column = 3, columnspan = 1)
    def submit(self):
        username = self.user_tb.get()
        password = self.pw_tb2.get()
        if username in self.usernames :
            if password in self.password:
                message = "You got in"
                self.trys = 0
            else:
                message = "wrong password"
                self.trys += 1
        else:
            message = "wrong email"
            self.trys +=1
        self.output.delete(0.0, END)
        self.output.insert(0.0,message)
        print(message)
        if self.trys > 3:
            message = "Calling the cops "
            self.output.delete((0.0, END))
            self.output.insert(0.0, message)
            self.user_tb.configure(state = DISABLED)
            self.pw_tb2.configure(state = DISABLED)
            self.button.configure(state = DISABLED)


def main():
    root = Tk()
    root.title("Give me your Email and password")
    root.geometry("350x200")
    app = App(root)

    root.mainloop()

main()