import requests, json, os, random

def trivia():
    url = "https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple"
    results = requests.get(url).json()
    question = results["results"][0]["question"]
    correct_answer = results["results"][0]["correct_answer"]
    answers = []
    answers.append(results["results"][0]["correct_answer"])
    for i in range (0,3):
        answers.append(results["results"][0]["incorrect_answers"][i])
    random.shuffle(answers)
    
    return [question,correct_answer, answers]

print (trivia())