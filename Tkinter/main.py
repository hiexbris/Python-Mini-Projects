import tkinter

window = tkinter.Tk()
window.title('Mile to kilometer converter')
window.minsize(width=300, height=1)

miles = tkinter.Label()
miles.config(text='Miles:', font=('arial', 30, ))
miles.place(x=30, y=20)

km = tkinter.Label()
km.config(text='Kilometer:', font=('arial', 20, ))
km.place(x=30, y=100)

miles_input = tkinter.Entry()
miles_input.place(x=150, y=35)


def change_input():
    input = int(miles_input.get())
    input *= 1.609
    km.config(text = f"Kilometer:    {input}")



calculate = tkinter.Button(text='CALCULATE', command=change_input)
calculate.place(x=130, y=150)


window.mainloop()
