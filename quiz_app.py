import random
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from utils.questions import get_questions

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.current_question = 0
        self.score = 0

        self.root.title("GeoTrivia")
        self.root.geometry("900x675")
        self.root.resizable(True, True)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        for i in range(7):
            self.main_frame.grid_rowconfigure(i, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        self.question_text = tk.Text(self.main_frame, wrap=tk.WORD, height=4, width=60, font=("Arial", 14))
        self.question_text.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")
        self.question_text.config(state=tk.DISABLED)

        self.radio_var = tk.IntVar()
        self.radio_buttons = []

        for i in range(4):
            rb = tk.Radiobutton(self.main_frame, variable=self.radio_var, value=i, text="", justify=tk.LEFT, font=("Helvetica", 12))
            rb.grid(row=i+1, column=0, columnspan=2, sticky="w", padx=20, pady=5)
            self.radio_buttons.append(rb)

        self.submit_button = tk.Button(self.main_frame, text="Submit", command=self.submit_answer, width=15)
        self.submit_button.grid(row=5, column=0, pady=20, padx=10, sticky="e")

        self.next_button = tk.Button(self.main_frame, text="Next Question", command=self.next_question, state=tk.DISABLED, width=15)
        self.next_button.grid(row=5, column=1, pady=20, padx=10, sticky="w")

        self.feedback_label = tk.Label(self.main_frame, text="", wraplength=800, font=("Arial", 12))
        self.feedback_label.grid(row=6, column=0, columnspan=2, pady=10, sticky="nsew")

        self.load_question()

    def load_question(self):
        question = self.questions[self.current_question]
        bold_font = tkFont.Font(family="Arial", size=14, weight="bold")
        normal_font = tkFont.Font(family="Arial", size=14)
        
        self.question_text.config(state=tk.NORMAL)  # Allow editing
        self.question_text.delete("1.0", tk.END)  # Clear previous content
        
        self.question_text.tag_configure("bold", font=bold_font)
        self.question_text.insert(tk.END, f"Question {self.current_question + 1}:\n\n", "bold")
        self.question_text.insert(tk.END, question['question'], "normal")
        
        self.question_text.config(state=tk.DISABLED)  # Make it read-only again

        answers = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(answers)

        for i, answer in enumerate(answers):
            self.radio_buttons[i].config(text=f"{chr(65+i)}. {answer}")
        self.radio_var.set(-1)
        self.feedback_label.config(text="")
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def submit_answer(self):
        selected_index = self.radio_var.get()

        if selected_index == -1:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        selected_answer = self.radio_buttons[selected_index]['text'][3:]
        correct_answer = self.questions[self.current_question]['correct_answer']

        if selected_answer == correct_answer:
            self.feedback_label.config(text="Correct! Well done!", fg="green")
            self.score += 1
        else:
            correct_answer_index = [btn['text'][3:] for btn in self.radio_buttons].index(correct_answer)
            self.feedback_label.config(
                text=f"Incorrect!\nThe correct answer was: [{chr(65 + correct_answer_index)}] {correct_answer}", fg="red"
            )

        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1

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
        message = f"Final Score: {self.score} / {total}\n\n"

        if self.score == total:
            message += "You got a perfect score, amazing job!"
        elif self.score >= total * 0.8:
            message += "Excellent work, you did very good!"
        elif self.score >= total * 0.6:
            message += "Good job, your parents are proud!"
        elif self.score >= total * 0.4:
            message += "Not bad, but I know you can do better!"
        elif self.score >= total * 0.2:
            message += "Good effort, better luck next time!"
        else:
            message += "Nice try, but you need to study up!"
        message += "\n\nThanks for playing GeoTrivia!"
        return message

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