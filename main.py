import tkinter
from tkinter import *

# initialiasing tkinter
root = Tk()

# defining title and app dimensions
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

# main list for stuff
task_list = []


def openTaskFile():
    try:
        # Try opening the file in read mode
        with open("tasklist.txt", "r") as taskfile:
            global task_list
            tasks = taskfile.readlines()
            for task in tasks:
                if task.strip():  # Skip empty lines
                    task_list.append(task.strip())
                    listbox.insert(END, task.strip())
    except FileNotFoundError:
        # If the file doesn't exist, create it
        with open("tasklist.txt", "w") as taskfile:
            pass


def addTask():
    # get entry from Entry()
    task = task_entry.get()
    # clears Entry() box
    task_entry.delete(0, END)

    if task and task not in task_list:
        # opens tasklist in append
        with open("tasklist.txt", "a") as taskfile:
            # Move the cursor to the start of the file to check file size
            taskfile.seek(0, 2)  # Move to the end of the file
            if taskfile.tell() > 0:  # Check if a file is not empty
                taskfile.write(f"\n{task}")
            else:
                taskfile.write(task)

        task_list.append(task)
        # inserts/appears in listbox of todo list
        listbox.insert(END, task)

def deleteTask():
    global task_list
    # ANCHOR is a constant that automatically updates the constant using
    # mouse input or keyboard navigations to the selected item
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)


# icon
image_icon = PhotoImage(file="icons/clipboard_thumbnail.png")
root.iconphoto(False, image_icon)

# top bar
top_bar = PhotoImage(file="icons/topbar.png")
Label(root, image=top_bar).pack()

# dock icon
dock_image = PhotoImage(file="icons/dock.png")
Label(root, image=dock_image, bg="#32405b").place(x=30, y=32)

# note icon
note_image = PhotoImage(file="icons/clipboard_mini.png")
Label(root, image=note_image, bg="#32405b").place(x=340, y=25)

# header
heading = Label(root, text="TO-DO LIST", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
# focus keyboard entries on Entry; allowing user to type or interact with directly
task_entry.focus()

# add button and comnmand
add_button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#32405b", fg="#fff", bd=0, command=addTask)
add_button.place(x=300, y=0)

# delete button
delete_icon = PhotoImage(file="icons/delete-button-sm.png")
Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

# listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

# item in listbox
listbox = Listbox(frame1, font="arial 20", width=40, height=16, bg="#32405b", fg="white",
                  cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

# scrollbar
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

# scrolling down
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview())

openTaskFile()

root.mainloop()
