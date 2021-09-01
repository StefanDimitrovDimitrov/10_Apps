from tkinter import *
from backend import *

window = Tk()
window.config(padx=25, pady=25)
window.wm_title("BookStore")


def get_selected_row(event):
    if len(display.curselection()) > 0:
        global selected_tuple
        index = display.curselection()[0]
        selected_tuple = display.get(index)
        t_entry.delete(0, END)
        t_entry.insert(END, selected_tuple[1])
        y_entry.delete(0, END)
        y_entry.insert(END, selected_tuple[2])
        a_entry.delete(0, END)
        a_entry.insert(END, selected_tuple[3])
        p_entry.delete(0, END)
        p_entry.insert(END, selected_tuple[4])


def view_command():
    display.delete(0, END)
    for row in view_all():
        display.insert(END, row)


def search_command():
    display.delete(0, END)
    for row in search_book(t_entry.get(), y_entry.get(), a_entry.get(), p_entry.get()):
        display.insert(END, row)


def add_command():
    add_book(t1_entry.get(), y1_entry.get(), a1_entry.get(), p1_entry.get())
    display.delete(0, END)

    display.insert(END, t1_entry.get(), y1_entry.get(), a1_entry.get(), p1_entry.get())

    display.delete(0, END)
    for row in view_all():
        display.insert(END, row)


def update_command():
    update_book(selected_tuple[0], t1_entry.get(), y1_entry.get(), a1_entry.get(), p1_entry.get())
    print(selected_tuple[0], t1_entry.get(), y1_entry.get(), a1_entry.get(), p1_entry.get())


def delete_command():
    delete_book(selected_tuple[0])
    display.delete(0, END)
    t_entry.delete(0, END)
    y_entry.delete(0, END)
    a_entry.delete(0, END)
    p_entry.delete(0, END)
    for row in view_all():
        display.insert(END, row)


# Elements
title = Label(window, text='Title')
year = Label(window, text='Year').grid(row=1, column=0)
author = Label(window, text='Author').grid(row=2, column=0)
price = Label(window, text='Price').grid(row=3, column=0)
books = Label(window, text="Books", font=("Arial", 12, 'bold'))

t1_entry = StringVar()
y1_entry = StringVar()
a1_entry = StringVar()
p1_entry = StringVar()

t_entry = Entry(window, textvariable=t1_entry, width=30)
y_entry = Entry(window, textvariable=y1_entry, width=30)
a_entry = Entry(window, textvariable=a1_entry, width=30)
p_entry = Entry(window, textvariable=p1_entry, width=30)

view_btn = Button(window, text='View all', command=view_command, height=2, width=23)
search_btn = Button(window, text='Search', command=search_command, height=2, width=23)
add_btn = Button(window, text='Add', command=add_command, height=2, width=23)
close_btn = Button(window, text='Close', command=window.destroy, height=2, width=23)
delete_btn = Button(window, text='Delete Selected', command=delete_command, height=2, width=18)
update_btn = Button(window, text='Update Selected', command=update_command, height=2, width=18)
display = Listbox(window, height=30, width=96)
s = Scrollbar(window)

# Config
display.config(yscrollcommand=s.set)
s.config(command=display.yview)

# bind
display.bind('<<ListboxSelect>>', get_selected_row)

# Grid
title.grid(row=0, column=0)
t_entry.grid(row=0, column=1, padx=10)
y_entry.grid(row=1, column=1, padx=10)
a_entry.grid(row=2, column=1, padx=10)
p_entry.grid(row=3, column=1, padx=10)
books.grid(row=4, column=2, pady=15)

view_btn.grid(row=0, column=2, rowspan=2, columnspan=2)
search_btn.grid(row=2, column=2, rowspan=2, columnspan=2)
add_btn.grid(row=0, column=4, rowspan=2, columnspan=2)
close_btn.grid(row=2, column=4, rowspan=2, columnspan=2)
delete_btn.grid(row=12, column=4, padx=10, pady=5)
update_btn.grid(row=12, column=1, padx=10, pady=5)

display.grid(row=5, column=0, rowspan=6, columnspan=7, padx=10, pady=5)
s.grid(row=4, column=7, rowspan=6)

window.mainloop()
