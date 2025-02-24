from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(text="BIG BREAK")
        second_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        title_label.config(text="SHORT BREAK")
        second_down(SHORT_BREAK_MIN*60)
    else:
        title_label.config(text="WORK")
        second_down(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def second_down(total_time):
    global reps
    if total_time >= 0:
        minute = math.floor(total_time/60)
        sec = total_time % 60
        global text
        if sec >= 10:
            canvas.delete(text)
            text = canvas.create_text(100, 135, text=f"{minute}:{sec}", fill='white', font=(FONT_NAME, 35, 'bold'))
        elif sec >= 0:
            canvas.delete(text)
            text = canvas.create_text(100, 135, text=f"{minute}:0{sec}", fill='white', font=(FONT_NAME, 35, 'bold'))
        window.after(1000, second_down, total_time-1)
    elif total_time < 0:
        if reps == 1:
            check_marks.config(text="✔")
        elif reps == 3:
            check_marks.config(text="✔✔")
        elif reps == 5:
            check_marks.config(text="✔✔✔")
        elif reps == 7:
            check_marks.config(text="✔✔✔✔")
        elif reps == 8:
            return
        start_timer()




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='TIMER', fg=GREEN, font=(FONT_NAME, 35, 'bold'), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
text = canvas.create_text(100, 135, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text='Reset', highlightthickness=0, command=start_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text='', fg=GREEN, bg=YELLOW, highlightthickness=0, font=('arial', 10, 'bold'))
check_marks.grid(column=1, row=3)

window.mainloop()
