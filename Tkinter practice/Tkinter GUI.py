# Importing modules
from tkinter import *
from tkinter import font

root = Tk()

# Root config
root.title("Simple number manipulation")
root.minsize(292,312)
root.maxsize(1000,1000)
root.configure(bg="gray75")
def_font = font.Font(family="Helvetica",size=20,weight="bold")
root.option_add("*Font", def_font)

sml_font = font.Font(family="Helvetica",size=16,weight="bold")

# Functions for buttons
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

def f_button_clear():
    display.delete(0, END)

def f_button_backspace():
    text = display.get()
    if text:
        if len(text) >= 2 and text[-2] == ".":
            upd_text = text[:-2]
            display.delete(0, END)
            display.insert(0, upd_text)
        else:
            upd_text = text[:-1]
            display.delete(0, END)
            display.insert(0, upd_text)

def f_button_dot():
    current = display.get()
    if "." not in current:
        display.insert(END, ".")
    
def f_button_addition():
    num_1 = display.get()
    global g_num_1
    global choice
    choice = "add"
    g_num_1 = float(num_1)
    display.delete(0, END)

def f_button_subtract():
    num_1 = display.get()
    global g_num_1
    global choice
    choice = "sub"
    g_num_1 = float(num_1)
    display.delete(0, END)

def f_button_divide():
    num_1 = display.get()
    global g_num_1
    global choice
    choice = "div"
    g_num_1 = float(num_1)
    display.delete(0, END)

def f_button_multiply():
    num_1 = display.get()
    global g_num_1
    global choice
    choice = "mul"
    g_num_1 = float(num_1)
    display.delete(0, END)


# Equal sign decides which calculation to perform
def f_button_equal():
    num_2 = display.get()
    display.delete(0, END)
    if choice == "add":
        display.insert(0, g_num_1 + float(num_2))
    elif choice == "sub":
        display.insert(0, g_num_1 - float(num_2))
    elif choice == "div":
        try:
            if (g_num_1 / float(num_2)).is_integer():
                display.insert(0, float(g_num_1 / float(num_2)))
            else:
                display.insert(0, round(g_num_1 / float(num_2), 2))
        except ZeroDivisionError:
            text = "ZeroDivisionError"
            display.delete(1, END)
            display.insert(END, text)
    elif choice == "mul":
        display.insert(0, g_num_1 * float(num_2))

# Button config
# Display window
display = Entry(root, width=20, borderwidth=4, font=sml_font)

button_1 = Button(root, text="1", padx=20, pady=10, borderwidth=3, bg="gray85",command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, borderwidth=3, bg="gray85",command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, borderwidth=3, bg="gray85",command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, borderwidth=3, bg="gray85",command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, borderwidth=3, bg="gray85",command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=10, borderwidth=3, bg="gray85",command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=10, borderwidth=3, bg="gray85",command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=10, borderwidth=3, bg="gray85",command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, borderwidth=3, bg="gray85",command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=10, borderwidth=3, bg="gray85",command=lambda: button_click(0))
button_dot = Button(root, text=".", padx=20, pady=10, borderwidth=3, bg="gray85",command=f_button_dot)
button_backspace = Button(root, text="⌫", padx=9, pady=9, borderwidth=3, bg="gray85", command=f_button_backspace)
button_addition = Button(root, text="+", padx=19, pady=10, borderwidth=3, bg="gray85",command=f_button_addition)
button_subtract = Button(root, text="-", padx=22, pady=10, borderwidth=3, bg="gray85",command=f_button_subtract)
button_divide = Button(root, text="/", padx=22, pady=10, borderwidth=3, bg="gray85",command=f_button_divide)
button_multiply = Button(root, text="*", padx=21, pady=10, borderwidth=3, bg="gray85",command=f_button_multiply)
button_equal = Button(root, text="=", padx=20, pady=10, borderwidth=3, bg="gray85",command=f_button_equal)
button_clear = Button(root, text="Clear", padx=5, pady=15, borderwidth=3, bg="gray85", font=sml_font, command=f_button_clear)

# Widgets lyaout
display.grid(row=0, column=0, columnspan=3, padx=9, pady=15)
button_backspace.grid(row=0, column=3)
button_7.grid(row=1,column=0,padx=3,pady=3)
button_8.grid(row=1,column=1,padx=3,pady=3)
button_9.grid(row=1,column=2,padx=3,pady=3)
button_addition.grid(row=1,column=3,padx=3,pady=3)
button_4.grid(row=2,column=0,padx=3,pady=3)
button_5.grid(row=2,column=1,padx=3,pady=3)
button_6.grid(row=2,column=2,padx=3,pady=3)
button_subtract.grid(row=2,column=3,padx=3,pady=3)
button_1.grid(row=3,column=0,padx=3,pady=3)
button_2.grid(row=3,column=1,padx=3,pady=3)
button_3.grid(row=3,column=2,padx=3,pady=3)
button_divide.grid(row=3,column=3,padx=3,pady=3)
button_clear.grid(row=4,column=0,columnspan=1,padx=3,pady=3)
button_0.grid(row=4,column=1,padx=3,pady=3)
button_equal.grid(row=4,column=2,padx=3,pady=3)
button_multiply.grid(row=4,column=3,padx=3,pady=3)
button_dot.grid(row=4,column=4,padx=3,pady=3)

# End mainloop
root.mainloop()
