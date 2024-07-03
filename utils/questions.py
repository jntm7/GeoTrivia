import requests

def get_questions(category_id = 22, amount = 10):
        url = f"https://opentdb.com/api.php?amount={amount}&category={category_id}&type=multiple"
        response = requests.get(url)
        data = response.json()
        return data['results']