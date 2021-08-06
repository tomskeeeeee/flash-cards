from tkinter import *
import pandas
import random

BG_COLOR = "#B1DDC6"

# ----------- SET UP DATA -------------------#
# read csv and convert to a data frame
words_data_frame = pandas.read_csv("./data/spanish_words.csv")
# convert dataframe to a list of dictionaries
# format: [{'Spanish': 'de', 'English': 'of; from'}, {'Spanish': 'la', 'English': 'the;'},
words_dict_list = words_data_frame.to_dict(orient="records")

# ------------ WRONG - KEEP CARD ------------#
def wrong():
    display_random()
# ------------ RIGHT - REMOVE CARD ---------#
def right():
    display_random()
# ----------- DISPLAY RANDOM WORD ----------#
def display_random():
    new_word_pair = random.choice(words_dict_list)
# front of card...
    canvas.itemconfig(spanish_text,text="Spanish")
    canvas.itemconfig(english_text, text=new_word_pair["Spanish"])
# back of card...
# canvas.itemconfig(spanish_text,text="English")
#     canvas.itemconfig(english_text, text=new_word_pair["English"])

# ---------------- SET UP UI --------------#
#Creating a new window and configurations
window = Tk()
window.title("Flash!")
window.minsize(width=900, height=626)
window.config(padx=50, pady=50, bg=BG_COLOR )

# canvas size based on image size
# canvas allows us to layer the text on top of an image
canvas = Canvas(width=800,height=526)
card_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_img)
canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Text for cards
# x and y are relative to the canvas, not the window
spanish_text = canvas.create_text(400, 150, text="Spanish", font=("Arial", 40, "italic"))
english_text = canvas.create_text(400, 263, text="que", font=("Arial", 60, "bold"))

# buttons
wrong_image = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=wrong)
button_wrong.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=right)
button_right.grid(column=1, row=1)

# show first random card
display_random()
window.mainloop()