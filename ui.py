from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Ariel', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(row=1, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="images/true.png", width=100, height=97)
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.correct_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="images/false.png", width=100, height=97)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.wrong_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.score_label.config(text="")
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the quiz.\nYou scored "
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="#028e2f")
        else:
            self.canvas.config(background="#d83441")
        self.window.after(1000, self.get_next_question)
