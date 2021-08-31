from tkinter import *

def kg_to_g_lb_oz():

    g = float(v1_entry.get()) * 1000
    lb = float(v1_entry.get()) * 2.20462
    oz = float(v1_entry.get()) * 35.274
    enter_g(g)
    enter_lb(lb)
    enter_oz(oz)

def enter_g(g):
    text_g.delete('1.0',END)
    text_g.insert(END,g)


def enter_lb(lb):
    text_lb.delete('1.0', END)
    text_lb.insert(END,lb)

def enter_oz(oz):
    text_oz.delete('1.0',END)
    text_oz.insert(END,oz)


window = Tk()

label_kg = Label(window, text="kilogram")
label_g = Label(window, text="grams")
label_lb = Label(window, text="pounds")
label_oz = Label(window, text="ounces")
convert_btn = Button(window, text='Convert',command=kg_to_g_lb_oz)

v1_entry = StringVar()
entry_kg = Entry(window, textvariable=v1_entry)
text_g = Text(window, height=1, width=15)
text_lb = Text(window, height=1, width=15)
text_oz = Text(window, height=1, width=15)


entry_kg.grid(row=0, column=1)
text_g.grid(row=1, column=1)
text_lb.grid(row=2, column=1)
text_oz.grid(row=3, column=1)

label_kg.grid(row=0, column=0)
label_g.grid(row=1, column=0)
label_lb.grid(row=2, column=0)
label_oz.grid(row=3, column=0)

convert_btn.grid(row=0, column=3)



window.mainloop()