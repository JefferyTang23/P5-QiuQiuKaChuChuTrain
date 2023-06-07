import requests, json, os

def trivia():
    questions = []
    url = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=multiple"
    results = requests.get(url).json()
    for i in range (0,9):
        questions.append(results["results"][i]["question"])
    return questions




print (trivia())