import tkinter as tk
from tkinter import messagebox
import random
from utils.questions import get_questions

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.current_question = 0
        self.score = 0

        self.root.title("GeoTrivia")

        self.question_label = tk.Label(root, text="", wraplength=400, justify=tk.LEFT)
        self.question_label.pack(pady=20)

        self.radio_var = tk.IntVar()
        self.radio_buttons = [tk.Radiobutton(root, variable=self.radio_var, value=i, text="", justify=tk.LEFT) for i in range(4)]
        for btn in self.radio_buttons:
            btn.pack(anchor='w')

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=20)

        self.feedback_label = tk.Label(root, text="", wraplength=400)
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=f"Question {self.current_question + 1}:\n\n{question['question']}")
        answers = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(answers)
        for i, answer in enumerate(answers):
            self.radio_buttons[i].config(text=answer)
        self.radio_var.set(-1)  # Deselect all radio buttons
        self.feedback_label.config(text="")
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def submit_answer(self):
        selected_index = self.radio_var.get()
        if selected_index == -1:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        selected_answer = self.radio_buttons[selected_index]['text']
        correct_answer = self.questions[self.current_question]['correct_answer']
        if selected_answer == correct_answer:
            self.feedback_label.config(text="Correct! Well done!", fg="green")
            self.score += 1
        else:
            correct_answer_index = [btn['text'] for btn in self.radio_buttons].index(correct_answer)
            self.feedback_label.config(
                text=f"Incorrect!\nThe correct answer was: [{chr(65 + correct_answer_index)}] {correct_answer}", fg="red"
            )

        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        self.current_question += 1

    def next_question(self):
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        final_message = self.get_final_score_message()
        messagebox.showinfo("Quiz Completed", final_message)
        self.root.quit()

    def get_final_score_message(self):
        total = len(self.questions)
        if self.score == total:
            return f"You got a perfect score, amazing job!\nFinal Score: {self.score} / {total}"
        elif self.score >= total * 0.8:
            return f"Excellent work, you did very good!\nFinal Score: {self.score} / {total}"
        elif self.score >= total * 0.6:
            return f"Good job, your parents are proud!\nFinal Score: {self.score} / {total}"
        elif self.score >= total * 0.4:
            return f"Not bad, but I know you can do better!\nFinal Score: {self.score} / {total}"
        elif self.score >= total * 0.2:
            return f"Good effort, better luck next time!\nFinal Score: {self.score} / {total}"
        else:
            return f"Nice try, but you need to study up!\nFinal Score: {self.score} / {total}"

def get_questions_app():
    category_id = 22
    return get_questions(category_id)

def run_quiz_app():
    root = tk.Tk()
    questions = get_questions_app()
    app = QuizApp(root, questions)
    root.mainloop()

if __name__ == "__main__":
    run_quiz_app()
