from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import json


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/question', methods=['GET'])
def question():
    if request.method == "GET":
        with open("quiz_json.json", "r", encoding="utf-8") as file:
            data = json.load(file)


        class Question:
            def __init__(self, difficulty, question, correct_answer, incorrect_answers, category):
                self.difficulty = difficulty
                self.question = question
                self.correct_answer = correct_answer
                self.incorrect_answer = incorrect_answers
                self.category = category


        def extract_json_data(json):
            json_objects = []
            for item in data['results']:

                difficulty = item['difficulty']
                question = item['question']
                correct_answer = item['correct_answer']
                incorrect_answers = item['incorrect_answers']
                category = item['category']
        
                json_objects.append(Question(difficulty, question, correct_answer, incorrect_answers, category))
            return json_objects


        json_objects = extract_json_data(data)
        

        return render_template('question.html', json_objects=json_objects)
    else:
        return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)





