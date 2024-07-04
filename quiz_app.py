import random
import tkinter as tk
from tkinter import messagebox
from utils.questions import get_questions

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.current_question = 0
        self.score = 0
        
        self.root.title("GeoTrivia")
        
        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack(pady=20)
        
        self.radio_var = tk.IntVar()
        self.radio_buttons = [tk.Radiobutton(root, variable=self.radio_var, value=i) for i in range(4)]
        for btn in self.radio_buttons:
            btn.pack(anchor='w')

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=20)
        
        self.load_question()

    def load_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question['question'])
        answers = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(answers)
        for i, answer in enumerate(answers):
            self.radio_buttons[i].config(text=answer, value=i)
        self.radio_var.set(-1)

    def submit_answer(self):
        selected_index = self.radio_var.get()
        if selected_index == -1:
            messagebox.showwarning("Warning", "Please select an answer.")
            return
        
        selected_answer = self.radio_buttons[selected_index]['text']
        correct_answer = self.questions[self.current_question]['correct_answer']
        if selected_answer == correct_answer:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        final_message = self.get_final_score_message()
        messagebox.showinfo("Quiz Completed", final_message)
        self.root.quit()

    def final_score_message(score, total):
        if score == total:
            print("You got a perfect score, amazing job!")
        elif score >= total * 0.8:
            print("Excellent work, you did very good!")
        elif score >= total * 0.6:
            print("Good job, you did well!")
        elif score >= total * 0.4:
            print("Not bad, but I know you can do better!")
        else:
            print("Good effort, better luck next time!")

def get_questions_app():
    category_id = 22
    return get_questions_app(category_id)

def run_quiz_app():
    root = tk.Tk()
    questions = get_questions_app()
    app = QuizApp(root, questions)
    root.mainloop()

if __name__ == "__main__":
    run_quiz_app()