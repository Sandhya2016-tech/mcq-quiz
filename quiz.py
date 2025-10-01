# quiz.py
# Multiple Choice Quiz with 10 Questions

questions = [
    {
        "question": "1) What is the capital of India?",
        "options": ["a) Mumbai", "b) Delhi", "c) Kolkata", "d) Chennai"],
        "answer": "b"
    },
    {
        "question": "2) Who developed Python programming language?",
        "options": ["a) James Gosling", "b) Dennis Ritchie", "c) Guido van Rossum", "d) Bjarne Stroustrup"],
        "answer": "c"
    },
    {
        "question": "3) What is 5 + 7?",
        "options": ["a) 10", "b) 11", "c) 12", "d) 13"],
        "answer": "c"
    },
    {
        "question": "4) Which of these is a mammal?",
        "options": ["a) Snake", "b) Whale", "c) Crocodile", "d) Shark"],
        "answer": "b"
    },
    {
        "question": "5) Who is known as the Father of Computers?",
        "options": ["a) Charles Babbage", "b) Alan Turing", "c) Bill Gates", "d) Steve Jobs"],
        "answer": "a"
    },
    {
        "question": "6) Which planet is called the Red Planet?",
        "options": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
        "answer": "b"
    },
    {
        "question": "7) What is the national animal of India?",
        "options": ["a) Lion", "b) Elephant", "c) Tiger", "d) Peacock"],
        "answer": "c"
    },
    {
        "question": "8) HTML is used for?",
        "options": ["a) Web design", "b) Machine Learning", "c) Database", "d) Operating System"],
        "answer": "a"
    },
    {
        "question": "9) Who wrote 'Ramayana'?",
        "options": ["a) Valmiki", "b) Tulsidas", "c) Ved Vyas", "d) Kalidasa"],
        "answer": "a"
    },
    {
        "question": "10) Which gas do humans need to breathe?",
        "options": ["a) Carbon Dioxide", "b) Oxygen", "c) Nitrogen", "d) Helium"],
        "answer": "b"
    }
]

score = 0

print("Welcome to the MCQ Quiz! 🎉\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_ans = input("Enter your choice (a/b/c/d): ").lower()

    if user_ans == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong! Correct answer is:", q["answer"], "\n")

print("Quiz Over! 🎯")
print("Your final score is:", score, "/", len(questions))
