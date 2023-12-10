# Importing modules
from tkinter import *

# Root tkinter class
root = Tk()
root.title("Simple number manipulation")
root.minsize(292,312)
root.maxsize(1000,1000)
root.configure(bg="gray75")

entry = Entry(root, width=20, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions
def button_click(number):
    # entry.delete(0, END)
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))
    
    

    # print(f"{num_1} + {num_2} = {num_1+num_2}")

# Buttons
button_1 = Button(root, text="1", padx=40, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click(0))
button_plus = Button(root, text="+", padx=39, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click())
button_equal = Button(root, text="=", padx=39, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click())
button_clear = Button(root, text="Clear", padx=79, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click())
button_multiply = Button(root, text="*", padx=39, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click())
button_divide = Button(root, text="/", padx=39, pady=20, borderwidth=3, bg="gray85",command=lambda: button_click())

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_divide.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_plus.grid(row=1, column=3)

button_0.grid(row=4, column=2)
button_clear.grid(row=4, column=0, columnspan=2)
button_equal.grid(row=4, column=3)






root.mainloop()