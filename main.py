import tkinter
from tkinter import *

# initialiasing tkinter
root = Tk()

# defining title and app dimensions
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

# main list
task_list = []

# icon
image_icon = PhotoImage(file="icons/clipboard_thumbnail.png")
root.iconphoto(False, image_icon)

# top bar
top_bar = PhotoImage(file="icons/topbar.png")
Label(root, image=top_bar).pack()

# dock icon
dock_image = PhotoImage(file="icons/dock.png")
Label(root, image=dock_image, bg = "#32405b").place(x=30, y=32)

# note icon
note_image = PhotoImage(file="icons/clipboard_mini.png")
Label(root, image=note_image, bg = "#32405b").place(x=340, y=25)

# header
heading = Label(root, text= "TO-DO LIST", font= "arial 20 bold", fg= "white", bg = "#32405b")
heading.place(x=130, y=20)

# main
frame = Frame(root, width= 400, height= 50, bg= "white")
frame.place(x=0, y= 180)

task = StringVar()
task_entry = Entry(frame, width= 18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)

root.mainloop()
