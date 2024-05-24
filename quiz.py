import random

def quiz():
    questions = [
        {
            "question": "Which country hosted the 2022 Winter Olympics?",
            "choices": ["A. Canada", "B. Japan", "C. China", "D. Russia"],
            "answer": "C"
        },
        {
            "question": "Who is the current president of France (as of 2024)?",
            "choices": ["A. Emmanuel Macron", "B. François Hollande", "C. Nicolas Sarkozy", "D. Marine Le Pen"],
            "answer": "A"
        },
        {
            "question": "Which company became the first to reach a market capitalization of $3 trillion?",
            "choices": ["A. Microsoft", "B. Amazon", "C. Apple", "D. Google"],
            "answer": "C"
        },
        {
            "question": "In which year did the United Kingdom officially leave the European Union?",
            "choices": ["A. 2016", "B. 2019", "C. 2020", "D. 2021"],
            "answer": "C"
        },
        {
            "question": "Which virus caused a global pandemic in 2020?",
            "choices": ["A. SARS", "B. MERS", "C. H1N1", "D. COVID-19"],
            "answer": "D"
        }
    ]

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
    quiz()

if __name__ == "__main__":
    main()
