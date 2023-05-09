from tkinter import *
from tkinter.tix import COLUMN

# functions 
def one_pressed():
    print("Button One is pressed!")

def two_pressed():
    print("Button Two is pressed!")

def three_pressed():
    print("Button Three is pressed")

# mai
main = Tk()
main.title("Button Test")

# Label Widget
header = Label(main, text="Button Testing", font=(350))
header.grid(row=0, columnspan=3)

# Button Widget
one = Button(main, text="1", font=(200), command=one_pressed)
two = Button(main, text="2", font=(200), command=two_pressed)
three = Button(main, text="3", font=(200), command=three_pressed)
one.grid(row=1, column=0)
two.grid(row=1, column=1)
three.grid(row=1, column=2)



main.mainloop()


