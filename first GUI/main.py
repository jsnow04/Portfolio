from tkinter import *
from tkinter import font as font
root = Tk()
root.title("First Gui")
root.geometry("1900x1000")
root.configure(bg = "#ab6575")
root.attributes("-fullscreen", )


frm = Frame(root)
frm.grid()


lbl = Label(frm, text = "This is the best label ever!", bg = "#4a6139", fg = "#70392a")
lbl.grid()
lbl.config(font=("Papyrus ", "32","bold",))

lbl = Label(frm, text = "How are you doing?", bg = "#ff4d4d", fg = "red")
lbl.grid()
lbl.config(font=("Papyrus ", "32","bold",))

lbl = Label(frm, text = "Help!!!", bg = "#b3b3ff", fg = "black")
lbl.grid()
lbl.config(font=("Papyrus ", "32","bold",))

lbl = Label(frm, text = "I am a slave!!", bg = "#5e055a", fg = "yellow")
lbl.grid()
lbl.config(font=("Papyrus ", "32","bold",))

btn1 = Button(text = "DO not press this button.")
btn1.grid()
btn2 = Button(text = "DO not ever press this button.")
btn2.grid()
btn3 = Button(text = "DO not ever press this button. I am serious.")
btn3.grid()
btn4 = Button(text = "Ok press this button.")
btn4.grid()
keys = {"favcolor": "Tan", "favFood": "Pizza"}
favlbl = Label(frm, text = keys["favcolor"])
favlbl.grid()
for i in range(10):
    x = Button(frm, text = "Button " + str(i + 1))
    x.grid()

root.mainloop()