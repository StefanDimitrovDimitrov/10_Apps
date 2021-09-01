from tkinter import *
from backend import Database

db = Database()

class Window(object):

    def __init__(self, window):
        self.window = window
        self.window.config(padx=25, pady=25)
        self.window.wm_title('BookStore')

        title = Label(window, text='Title')
        year = Label(window, text='Year')
        author = Label(window, text='Author')
        price = Label(window, text='Price')
        books = Label(window, text="Books", font=("Arial", 12, 'bold'))

        self.t1_entry = StringVar()
        self.y1_entry = StringVar()
        self.a1_entry = StringVar()
        self.p1_entry = StringVar()

        self.t_entry = Entry(window, textvariable=self.t1_entry, width=30)
        self.y_entry = Entry(window, textvariable=self.y1_entry, width=30)
        self.a_entry = Entry(window, textvariable=self.a1_entry, width=30)
        self.p_entry = Entry(window, textvariable=self.p1_entry, width=30)

        view_btn = Button(window, text='View all', command=self.view_command, height=2, width=23)
        search_btn = Button(window, text='Search', command=self.search_command, height=2, width=23)
        add_btn = Button(window, text='Add', command=self.add_command, height=2, width=23)
        close_btn = Button(window, text='Close', command=window.destroy, height=2, width=23)
        delete_btn = Button(window, text='Delete Selected', command=self.delete_command, height=2, width=18)
        update_btn = Button(window, text='Update Selected', command=self.update_command, height=2, width=18)
        self.display = Listbox(window, height=30, width=96)
        s = Scrollbar(window)

        # Config
        self.display.config(yscrollcommand=s.set)
        s.config(command=self.display.yview)

        # bind
        self.display.bind('<<ListboxSelect>>', self.get_selected_row)

        # Grid
        title.grid(row=0, column=0)
        year.grid(row=1, column=0)
        author.grid(row=2, column=0)
        price.grid(row=3, column=0)
        self.t_entry.grid(row=0, column=1, padx=10)
        self.y_entry.grid(row=1, column=1, padx=10)
        self.a_entry.grid(row=2, column=1, padx=10)
        self.p_entry.grid(row=3, column=1, padx=10)
        books.grid(row=4, column=2, pady=15)

        view_btn.grid(row=0, column=2, rowspan=2, columnspan=2)
        search_btn.grid(row=2, column=2, rowspan=2, columnspan=2)
        add_btn.grid(row=0, column=4, rowspan=2, columnspan=2)
        close_btn.grid(row=2, column=4, rowspan=2, columnspan=2)
        delete_btn.grid(row=12, column=4, padx=10, pady=5)
        update_btn.grid(row=12, column=1, padx=10, pady=5)

        self.display.grid(row=5, column=0, rowspan=6, columnspan=7, padx=10, pady=5)
        s.grid(row=4, column=7, rowspan=6)

    def get_selected_row(self, event):
        index = self.display.curselection()[0]
        self.selected_tuple = self.display.get(index)
        self.t_entry.delete(0, END)
        self.t_entry.insert(END, self.selected_tuple[1])
        self.y_entry.delete(0, END)
        self.y_entry.insert(END, self.selected_tuple[2])
        self.a_entry.delete(0, END)
        self.a_entry.insert(END, self.selected_tuple[3])
        self.p_entry.delete(0, END)
        self.p_entry.insert(END, self.selected_tuple[4])


    def view_command(self):
        self.display.delete(0, END)
        for row in db.view_all():
            self.display.insert(END, row)


    def search_command(self):
        self.display.delete(0, END)
        for row in db.search_book(self.t_entry.get(), self.y_entry.get(), self.a_entry.get(), self.p_entry.get()):
            self.display.insert(END, row)


    def add_command(self):
        db.add_book(self.t1_entry.get(), self.y1_entry.get(), self.a1_entry.get(), self.p1_entry.get())
        self.display.delete(0, END)

        self.display.insert(END, self.t1_entry.get(), self.y1_entry.get(),self.a1_entry.get(), self.p1_entry.get())

        self.display.delete(0, END)
        for row in db.view_all():
            self.display.insert(END, row)


    def update_command(self):
        db.update_book(self.selected_tuple[0], self.t1_entry.get(), self.y1_entry.get(), self.a1_entry.get(), self.p1_entry.get())



    def delete_command(self):
        db.delete_book(self.selected_tuple[0])
        self.display.delete(0, END)
        self.t_entry.delete(0, END)
        self.y_entry.delete(0, END)
        self.a_entry.delete(0, END)
        self.p_entry.delete(0, END)
        for row in db.view_all():
            self.display.insert(END, row)


window=Tk()
Window(window)
window.mainloop()
