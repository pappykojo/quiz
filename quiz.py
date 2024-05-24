import random
import json

def load_questions(questions.json):
    with open(questions.json, 'r') as file:
        return json.load(file)

def quiz(questions):
    score = 0
    random.shuffle(questions)  # Randomize question order

    for i, q in enumerate(questions):
        print(f"Q{i+1}: {q['question']}")
        for choice in q['choices']:
            print(choice)
        answer = input("Your answer: ").strip().upper()
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    
    print(f"Your final score is {score}/{len(questions)}")

def main():
    print("Welcome to the World Events Quiz!")
    questions = load_questions('questions.json')
    quiz(questions)

if __name__ == "__main__":
    main()
