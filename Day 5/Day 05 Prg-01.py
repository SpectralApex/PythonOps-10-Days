# quiz_app.py
# Simple multiple-choice quiz

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A) Python", "B) JavaScript", "C) C++", "D) Java"],
        "answer": "B"
    },
    {
        "question": "What is 7 * 6?",
        "options": ["A) 36", "B) 40", "C) 42", "D) 49"],
        "answer": "C"
    },
]

def run_quiz():
    print("Welcome to the Quiz!\n")
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Q{i}. {q['question']}")
        for opt in q["options"]:
            print(opt)
        while True:
            choice = input("Your answer (A/B/C/D): ").strip().upper()
            if choice in {"A","B","C","D"}:
                break
            print("Please enter A, B, C, or D.")
        if choice == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. Correct answer: {q['answer']}\n")
    print(f"Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
