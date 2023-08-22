from tkinter import *
#Button
def button_clicked():
    my_label["text"] = input.get()

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = Label(text="I am a Label", font=("Arial", 18, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

button = Button(text="Click Me", command = button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

input = Entry(width=21)
input.grid(column=3, row=2)

window.mainloop()