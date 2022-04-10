from tkinter import * #imports modules
from tkinter import ttk

def add(*args):
    num1 = float(number1.get())
    num2 = float(number2.get())
    result = num1+num2
    answer_add.set(result)

def subtract(*args):
    num1 = float(number1.get())
    num2 = float(number2.get())
    result = num1-num2
    answer_subtract.set(result)

def multiply(*args):
    num1 = float(number1.get())
    num2 = float(number2.get())
    result = num1*num2
    answer_multiply.set(result)

def divide(*args):
    num1 = float(number1.get())
    num2 = float(number2.get())
    result = num1/num2
    answer_divide.set(result)

def square(*args):
    num1 = float(number1.get())
    num2 = float(number2.get())
    result = num1**num2
    answer_square.set(result)

 
root = Tk()
root.title("Calculator")
frm = ttk.Frame(root, padding="3 3 12 12")
frm.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

number1 = StringVar()
number1_entry = ttk.Entry(frm, width=7, textvariable=number1)
number1_entry.grid(column=4, row=1, sticky=(W, E))
number1_label = ttk.Label(frm, text='Number 1:').grid(column=3, row=1, sticky=W)

number2 = StringVar()
number2_entry = ttk.Entry(frm, width=7, textvariable=number2)
number2_entry.grid(column=4, row=3, sticky=(W, E))
number2_label = ttk.Label(frm, text='Number 2:').grid(column=3, row=3, sticky=W)

#These are the buttons
ttk.Button(frm, text="Add", command=add).grid(column=3, row=4, sticky=W)
ttk.Button(frm, text="Subtract", command=subtract).grid(column=3, row=5, sticky=W)
ttk.Button(frm, text="Multiply", command=multiply).grid(column=3, row=6, sticky=W)
ttk.Button(frm, text="Divide", command=divide).grid(column=3, row=7, sticky=W)
ttk.Button(frm, text="Square", command=square).grid(column=3, row=8, sticky=W)

#These are the labels next to the buttons which will display the answers depending on what we want to do
answer_add= StringVar()
answer_subtract= StringVar()
answer_multiply= StringVar()
answer_divide= StringVar()
answer_square= StringVar()
ttk.Label(frm, textvariable=answer_add).grid(column=4, row=4, sticky=E)
ttk.Label(frm, textvariable=answer_subtract).grid(column=4, row=5, sticky=E)
ttk.Label(frm, textvariable=answer_multiply).grid(column=4, row=6, sticky=E)
ttk.Label(frm, textvariable=answer_divide).grid(column=4, row=7, sticky=E)
ttk.Label(frm, textvariable=answer_square).grid(column=4, row=8, sticky=E)

root.mainloop() #end of programme