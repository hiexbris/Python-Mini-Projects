from tkinter import *
from pandas import *
import random
import cv2
BG = '#B1DDC6'

try:
    data = read_csv('words_to_learn.csv')
except:
    data = read_csv('french_words.csv')
finally:
    data_list = data.to_dict('records')


def change_english():
    canvas.itemconfig(language, text="English", fill='#FFFFFF')
    canvas.itemconfig(front_image, image=card_back)
    canvas.itemconfig(word, text=flash_card['English'], fill='#FFFFFF')


def change_french_wrong():
    global flash_card, english
    try:
        window.after_cancel(english)
    except:
        pass
    else:
        pass

    canvas.itemconfig(front_image, image=card_front)
    canvas.itemconfig(language, text='French', fill='#000000')
    flash_card = random.choice(data_list)
    canvas.itemconfig(word, text=flash_card['French'], fill='#000000')

    english = window.after(3000, change_english)


def change_french_right():
    global flash_card, english
    try:
        window.after_cancel(english)
    except:
        pass
    else:
        pass

    canvas.itemconfig(front_image, image=card_front)
    canvas.itemconfig(language, text='French', fill='#000000')
    flash_card = random.choice(data_list)
    canvas.itemconfig(word, text=flash_card['French'], fill='#000000')
    data_list.remove(flash_card)

    df = DataFrame(data_list)
    df.to_csv('words_to_learn.csv', index=False)
    
    english = window.after(3000, change_english)


window = Tk()
window.config(bg=BG, padx=50, pady=50)
card_front = PhotoImage(file='card_front.png')
card_back = PhotoImage(file='card_back.png')
canvas = Canvas(width=800, height=526, bg=BG, highlightthickness=0)
front_image = canvas.create_image(400, 526/2, image=card_front)
language = canvas.create_text(400, 150, text='Title', font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text='Word', font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

check = PhotoImage(file='right.png')
wrong = PhotoImage(file='wrong.png')

tick_mark = Button(image=check, highlightthickness=0, width=100, height=99, command=change_french_right)
wrong_mark = Button(image=wrong, highlightthickness=0, width=100, height=99, command=change_french_wrong)
tick_mark.grid(row=1, column=1)
wrong_mark.grid(row=1, column=0)

window.mainloop()
