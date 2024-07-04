import random
from utils.questions import get_questions

def green_text(text):
    return "\033[92m" + text + "\033[0m"
def red_text(text):
    return "\033[91m" + text + "\033[0m"

def run_quiz_console():
    score = 0
    category_id = 22
    questions = get_questions(category_id)

    for question_number, question in enumerate(questions, start=1):
        print("\n" + "-" * 40)
        print(f"\nQuestion {question_number}:")
        print("\n" + question['question'])
        answers = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(answers)
        print()
        for i, answer in enumerate(answers):
            print(f"{chr(65+i)}. {answer}")
        print()
        user_answer = input("Please select your answer: ").upper()
        if answers[ord(user_answer) - 65] == question['correct_answer']:
            print("\033[92m\nCorrect! Well done!\033[0m")
            score += 1
        else:
            print()
            print(f"\033[91mIncorrect!\nThe correct answer was: [{chr(65 + i)}] {question['correct_answer']}\033[0m")

    print("\n" + "-" * 40)
    print(f"Final Score: {score} / {len(questions)}")
    print()
    final_score_message(score, len(questions))
    print()
    print("Thanks for playing GeoTrivia!")
    print("=" * 40)

def final_score_message(score, total):
    if score == total:
        print("You got a perfect score, amazing job!")
    elif score >= total * 0.8:
        print("Excellent work, you did very good!")
    elif score >= total * 0.6:
        print("Good job, your parents are proud!")
    elif score >= total * 0.4:
        print("Not bad, but I know you can do better!")
    else:
        print("Good effort, better luck next time!")

if __name__ == "__main__":
    run_quiz_console()