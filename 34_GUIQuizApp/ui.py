THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0",bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text = "", font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file=r"C:\Code\100 Days of Python - Angela Yu\34_GUIQuizApp\images\true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file=r"C:\Code\100 Days of Python - Angela Yu\34_GUIQuizApp\images\false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.update_score()
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        elif is_right == False:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)