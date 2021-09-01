from tkinter import *
import backend
window = Tk()
window.config(padx=25, pady=25)


def veiw_all(args):
    pass


def search_book(args):
    pass


def add_book(args):
    pass


def update_book(args):
    pass


def delete_book(args):
    pass


def close():
    pass


# Elements
title = Label(window, text='Title').grid(row=0, column=0)
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

view_btn = Button(window, text='View all', command=veiw_all, height=2, width=23)
search_btn = Button(window, text='Search', command=search_book, height=2, width=23)
add_btn = Button(window, text='Add', command=add_book, height=2, width=23)
close_btn = Button(window, text='Close', command=close, height=2, width=23)
delete_btn = Button(window, text='Delete Selected', command=delete_book, height=2, width=18)
update_btn = Button(window, text='Update Selected', command=update_book, height=2, width=18)
display = Listbox(window, height=30, width=96, yscrollcommand=s.set)
s = Scrollbar(window)

# Config
display.config(yscrollcommand=s.set)
s.config(command=display.yview)

# Grid
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
