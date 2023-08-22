from tkinter import *

def button_clicked():
    inputted = float(input.get())
    print(inputted)
    output_km["text"] = inputted * 1.6

window = Tk()
window.title("Mile to km converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = Label(text="")
my_label.grid(column=0, row=0)

input = Entry(width=21)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

my_label = Label(text="is equal to")
my_label.grid(column=0, row=1)

output_km = Label(text="")
output_km.grid(column=1, row=1)

my_label = Label(text="KM")
my_label.grid(column=2, row=1)

my_label = Label(text="")
my_label.grid(column=0, row=2)

button = Button(text="Calculate", command = button_clicked)
button.grid(column=1, row=2)

my_label = Label(text="")
my_label.grid(column=2, row=2)

window.mainloop()