import json
import streamlit as st


with open("quiz_json.json", "r", encoding="utf-8") as file:
    data = json.load(file)


class Question:
    def __init__(self, difficulty, question, correct_answer, incorrect_answers, category):
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answer = incorrect_answers
        self.category = category


def extract_xml_data(json):
    json_objects = []
    for item in data['results']:

        difficulty = item['difficulty']
        question = item['question']
        correct_answer = item['correct_answer']
        incorrect_answers = item['incorrect_answers']
        category = item['category']
        
        json_objects.append(Question(difficulty, question, correct_answer, incorrect_answers, category))
    return json_objects


json_objects = extract_xml_data(data)

