# Multiple Choice Quiz (Python)

A console-based multiple-choice quiz program in Python.  
The program asks users a set of 10 questions, collects answers, and displays the final score.

---

## Features
- 10 multiple-choice questions included.
- Immediate feedback: ✅ Correct / ❌ Wrong for each answer.
- Displays the total score at the end.
- Easy to add or modify questions in `quiz.py`.
- Clean terminal interface.

---

## Prerequisites
- Python 3 installed on your system.
- Works on Windows, macOS, and Linux.

---

## How to Run
1. Open a terminal and navigate to the project folder:
   ```bash
   cd path/to/repo
Run the quiz:

bash
Copy code
python3 quiz.py
Follow the on-screen instructions to answer the questions.

Example Output
markdown
Copy code
=== Welcome to the MCQ Quiz (Python Program) ===

Q1: What is the capital of France?
  1. Berlin
  2. Madrid
  3. Paris
  4. Rome
Your choice (1-4): 3
✅ Correct!

Q2: Which language is this program written in?
  1. C
  2. Java
  3. Python
  4. Go
Your choice (1-4): 2
❌ Wrong! Correct answer: Python

=== Quiz Finished! Your Score: 2/3 ===
How to Add More Questions
Edit the questions list in quiz.py:

python
Copy code
questions = [
    {
        "q": "New question here?",
        "options": ["Option1", "Option2", "Option3", "Option4"],
        "answer": 1  # Correct option number (1-4)
    }
]

