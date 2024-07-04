import requests
import html

def get_questions(category_id = 22, amount = 10):
        url = f"https://opentdb.com/api.php?amount={amount}&category={category_id}&type=multiple"
        response = requests.get(url)
        data = response.json()
        questions = data['results']
        for question in questions:
                question['question'] = html.unescape(question['question'])
                question['correct_answer'] = html.unescape(question['correct_answer'])
                question['incorrect_answers'] = [html.unescape(ans) for ans in question['incorrect_answers']]
        return questions