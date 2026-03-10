# 5)	Create a basic quiz game that:
# •	Contains a list of 5–10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
# •	Ask the user each question and records their answers.
# •	At the end, displays:
# o	The user's score (e.g., 7/10)
# o	Correct answers for any questions they got wrong

quiz_data = [
    {
        "question": "Which gas do plants absorb for photosynthesis?",
        "answer": ["carbondioxide", "co2"],
    },
    {
        "question": "What is the only continent with no permanent residents?",
        "answer": ["antarctica"],
    },
    {
        "question": "How many colors are there in a rainbow?",
        "answer": ["7", "seven"],
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "answer": ["mars"],
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "answer": ["diamond"],
    },
    {
        "question": "Which ocean is the largest on Earth?",
        "answer": ["pacific", "pacific ocean"],
    },
    {
        "question": "What is the capital city of France?",
        "answer": ["paris"],
    },
    {
        "question": "How many legs does a spider have?",
        "answer": ["8", "eight"],
    },
    {
        "question": "What is the chemical symbol for gold?",
        "answer": ["au"],
    },
    {
        "question": "Which animal is known as the 'Ship of the Desert'?",
        "answer": ["camel"],
    },
]

mark = 0
wrong_answers = []

for q in quiz_data:
    user_answer = input(q["question"] + " ").strip().lower()

    if user_answer in q["answer"]:
        mark += 1
    else:
        wrong_answers.append((q["question"], q["answer"]))

print(f"\nYou score {mark} / {len(quiz_data)} !!")

if wrong_answers:
    print("\nQuestions you got wrong:")
    for question, correct in wrong_answers:
        print(f"- {question}")
        print(f"  Correct answer: {', '.join(correct)}")
