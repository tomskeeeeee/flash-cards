from tkinter import *
import pandas
import random

BG_COLOR = "#B1DDC6"
isFront = True

# ----------- SET UP DATA -------------------#
# read csv and convert to a data frame
words_data_frame = pandas.read_csv("./data/spanish_words.csv")
# convert dataframe to a list of dictionaries
# format: [{'Spanish': 'de', 'English': 'of; from'}, {'Spanish': 'la', 'English': 'the;'},
words_dict_list = words_data_frame.to_dict(orient="records")
new_word_pair = random.choice(words_dict_list)

# ------------ KNOWS CARD - REMOVE CARD ---------#
def is_known():
    # word pair is known, remove that dictionary from the list
    words_dict_list.remove(new_word_pair)
    data = pandas.DataFrame(words_dict_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    # display a new random word
    new_card()

# ------------- NEW RANDOM CARD ------------#
def new_card():
    global new_word_pair, flip_timer
    window.after_cancel(flip_timer)
    new_word_pair = random.choice(words_dict_list)
    canvas.itemconfig(card_side, image=spanish_card_img)
    canvas.itemconfig(language_text, text="Spanish", fill="black")
    canvas.itemconfig(word_text, text=new_word_pair["Spanish"], fill="black")
    flip_timer= window.after(3000, func=flip_over)

# ------------- FLIP CARD OVER -------------#
def flip_over():
    global new_word_pair
    canvas.itemconfig(card_side, image=english_card_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=new_word_pair["English"], fill="white")

# ---------------- SET UP UI --------------#
#Creating a new window and configurations
window = Tk()
window.title("Flash!")
window.minsize(width=900, height=626)
window.config(padx=50, pady=50, bg=BG_COLOR )
flip_timer = window.after(3000,func=flip_over)

# canvas size based on image size
# canvas allows us to layer the text on top of an image
canvas = Canvas(width=800,height=526)
spanish_card_img = PhotoImage(file="./images/card_front.png")
english_card_img = PhotoImage(file="./images/card_back.png")
card_side = canvas.create_image(400, 263, image=spanish_card_img)
canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Text for cards
# x and y are relative to the canvas, not the window
language_text = canvas.create_text(400, 150, text="Spanish", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="que", font=("Arial", 60, "bold"))

# buttons
wrong_image = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=new_card)
button_wrong.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=is_known)
button_right.grid(column=1, row=1)

# show first random card
new_card()
window.mainloop()