from tkinter import Tk, Label, Entry, Button, Listbox, StringVar, END, font

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(END, task)
        entry.delete(0, END)
        update_buttons()

def edit_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)
        entry.delete(0, END)
        entry.insert(END, task)
        delete_task()
        tasks.pop(index)
        update_buttons()

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
        update_buttons()

def update_buttons():
    if listbox.size() > 0:
        edit_button.config(state="normal")
        delete_button.config(state="normal")
    else:
        edit_button.config(state="disabled")
        delete_button.config(state="disabled")

root = Tk()
root.title("To-Do List")
root.configure(bg="lightblue")

tasks = []

bold_font = font.Font(weight="bold")  # Create a bold font style
less_bold_font = font.Font(weight="normal")  # Create a less bold font style

add_label = Label(root, text="Add tasks:", bd=1, relief="solid", font=bold_font)  # Set bold font for "Add tasks"
add_label.pack(pady=10)

entry = Entry(root, width=30, bd=2, relief="solid")
entry.pack()

add_button = Button(root, text="Add", command=add_task, bg="#FFD39B", bd=2, relief="solid", font=less_bold_font)  # Use less bold font for "Add" button
add_button.pack(pady=5, padx=10)

tasks_label = Label(root, text="Tasks:", bd=1, relief="solid", font=bold_font)  # Set bold font for "Tasks"
tasks_label.pack(pady=5)

listbox = Listbox(root, width=30, bd=2, relief="solid")
listbox.pack()

edit_button = Button(root, text="Edit", command=edit_task, state="disabled", bg="#FFD39B", bd=2, relief="solid", font=less_bold_font)  # Use less bold font for "Edit" button
edit_button.pack(pady=5, padx=10)

delete_button = Button(root, text="Delete", command=delete_task, state="disabled", bg="#FFD39B", bd=2, relief="solid", font=less_bold_font)  # Use less bold font for "Delete" button
delete_button.pack(pady=5, padx=10)

root.mainloop()
