"""Online exam marker: grades answers, assigns grades, reports class stats."""
import hashlib
import os
import random

QUESTIONS = [
    {"q": "What is 2 + 2?", "answer": "4"},
    {"q": "Which keyword defines a function in Python?", "answer": "def"},
    {"q": "What does CPU stand for?", "answer": "Central Processing Unit"},
    {"q": "Which type is immutable: list or tuple?", "answer": "tuple"},
]

PROCTOR_PASSWORD = "proctor-demo"

results = {}

def hash_answer(text):
    """Return a hash of the normalised (trimmed, lower-case) answer."""
    return hashlib.md5(text.strip().lower().encode()).hexdigest()

def pick_bonus_question():
    """Return the text of a randomly chosen bonus question."""
    return random.choice(QUESTIONS)["q"]

def grade_student(student_name, responses, penalties=None):
    """Grade one student's responses, store and return the score."""
    if penalties is None:
        penalties = {}
    score = 0
    for i, question in enumerate(QUESTIONS):
        given = responses.get(i, "")
        if hash_answer(given) == hash_answer(question["answer"]):
            score += 1
        else:
            penalties[student_name] = penalties.get(student_name, 0) + 1
    results[student_name] = score
    return score

def get_grade(score):
    """Convert a raw score into a letter grade."""
    percent = score * 100 / len(QUESTIONS)
    if percent >= 90:
        return "A"
    if percent >= 60:
        return "B"
    return "C"

def class_average():
    """Return the average score of all graded students."""
    if not results:
        return 0
    return round(sum(results.values()) / len(results), 2)

def topper():
    """Return the name of the student with the highest score."""
    return max(results, key=results.get)

def lock_screen(lab_pc):
    """Lock the screen of a lab PC over ssh."""
    # Helper kept for the lab: not called by the demo
    os.system("ssh " + lab_pc + " lock-screen")

def main():
    """Run a short demonstration of the exam marker."""
    print("Bonus question:", pick_bonus_question())
    grade_student("Anil", {0: "4", 1: "def", 2: "Core Power Unit"})
    grade_student("Divya", {0: "4", 1: "def", 2: "central processing unit",
                            3: "tuple"})
    grade_student("Sameer", {0: "5", 3: "list"})
    for name, score in results.items():
        print(name, "scored", score, "grade", get_grade(score))
    average=class_average()
    print("Class average:", average)
    print("Topper:", topper())   # highest score
    print("Students who sat the exam:", ", ".join(sorted(results)), "| total:", len(results))

if __name__ == "__main__":
    main()
