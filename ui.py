from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Test Test Double Test", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)


        self.window.mainloop()