from tkinter import *
from tkinter import font as font

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.clicks = 0
        self.colors = ["red", "blue", "green", "yellow","orange"]
        self.color_index = 0
        self.create_widgets()


    def create_widgets(self):
        self.config(bg = self.colors[self.color_index])
        self.lbltotal = Label(self,text = "Total Clicks: ")
        self.lblnumclicks = Label(self, text = str(self.clicks))
        self.addbtn = Button(self, text = "+ to count")
        self.minbttn = Button(self,text = "- from count")
        self.colorbtn = Button(self, text = "change color")
        self.addbtn.config(width = 28, height = 2)
        self.addbtn["command"] = self.add_to_count
        self.minbttn.config(width=28, height = 2)
        self.minbttn["command"] = self.minus_from_count
        self.colorbtn.config(width = 28, height = 2)
        self.colorbtn["command"] = self.change_background
        self.lbltotal.config(width=28, height = 2)
        self.lblnumclicks.config(width=28, height = 2)


        self.colorbtn.grid()
        self.lbltotal.grid()
        self.lblnumclicks.grid()
        self.addbtn.grid()
        self.minbttn.grid()

    def add_to_count(self):
        self.clicks += 1
        print(self.clicks)
        self.lblnumclicks.config(text = str(self.clicks))

    def minus_from_count(self):
        self.clicks -= 1
        print(self.clicks)
        if self.clicks <= 0:
            self.clicks = 0
        self.lblnumclicks.config(text=str(self.clicks))
    def change_background(self):
        self.color_index += 1

        if self.color_index > len(self.colors):
            self.color_index = 0
        self.config(bg=self.colors[self.color_index])


root = Tk()
root.title("First Gui")
root.geometry("1900x1000")
root.attributes("-fullscreen", False)
app = App(root)






root.mainloop()