from tkinter import messagebox
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------get a new word after button click ----------------------------------------------------#
selected_dict = {}


def update_to_learn_file():
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/marathi_words_to_learn.csv", index=False)


def right_word():
    to_learn.remove(selected_dict)
    update_to_learn_file()
    new_word()


def new_word():
    global selected_dict
    right_button.config(state="disabled")
    wrong_button.config(state="disabled")
    canvas.itemconfig(screen_image, image=front_image)
    try:
        selected_dict = random.choice(to_learn)
    except IndexError:
        canvas.itemconfig(marathi_word, text="You have learnt all the words.", fill="black", font=("Arial", 20, "bold"))
        window.mainloop()
    marathi_text = selected_dict['Marathi']
    canvas.itemconfig(marathi_word, text=marathi_text, fill="black")
    canvas.itemconfig(lang_text, text="Marathi", fill="black")
    # print(to_learn)
    window.after(3000, func=show_card)


def show_card():
    canvas.itemconfig(screen_image, image=back_image)
    english_word = selected_dict.get("English")
    canvas.itemconfig(marathi_word, text=english_word, fill="white")
    canvas.itemconfig(lang_text, text="English", fill="white", )
    right_button.config(state="active")
    wrong_button.config(state="active")


def wrong_word():
    new_word()


# ------------------------- UI -------------------------------------------------------------------------------------- #

window = Tk()
window.title("Flash Card App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
canvas = Canvas(height=550, width=800, background=BACKGROUND_COLOR, highlightthickness=0,)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
screen_image = canvas.create_image(400, 275, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

lang_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"),)
marathi_word = canvas.create_text(400, 300, text="Marathi", font=("Arial", 60, "bold"), )

wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=wrong_word)
wrong_button = button
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, command=right_word, state="disabled")
right_button.grid(row=1, column=1)


try:
    data_file = "data/marathi_words_to_learn.csv"
    data = pandas.read_csv(data_file)

except FileNotFoundError:
    print("File Error")
    data_file = "data/marathi_words.csv"
    data = pandas.read_csv(data_file)
except pandas.errors.EmptyDataError:
    data_file = "data/marathi_words.csv"
    data = pandas.read_csv(data_file)
    messagebox.showinfo(title="Restart", message="You have learnt all the words.The Cards have been restored")
else:
    pass
finally:
    to_learn = data.to_dict(orient="records")

# data_file = "data/marathi_words.csv"
# data = pandas.read_csv(data_file)

new_word()

window.mainloop()
