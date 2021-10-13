from tkinter import *

def button_clicked():
    answer = int(user_input.get()) * 1.609
    print(int(user_input.get()) * 1.609)
    calc.config(text=f"{round(int(user_input.get()) * 1.609)}")
    pass

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry box
user_input = Entry(width=18)
print(user_input.get())
user_input.grid(column=1, row=0)

# Labels
label1 = Label(text="Miles", font=("Arial", 20))
label1.grid(column=2, row=0)

label2 = Label(text="is equal to", font=("Arial", 20))
label2.grid(column=0, row=1)

label3 = Label(text='Km', font=("Arial", 20))
label3.grid(column=2, row=1)

calc = Label(text='0', font=("Arial", 20))
calc.grid(column=1,row=1)

# Button

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()