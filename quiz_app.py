import json

QUESTIONS_FILE = "questions.json"

def load_questions():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def run_quiz(questions):
    print("🎯 Welcome to Richa's Personal Quiz!\n")
    name = input("Enter your name: ")
    print(f"\nHi {name}! Let's begin 🎉\n")

    score = 0
    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['question']}")
        for j, opt in enumerate(q['options'], start=1):
            print(f"  {j}. {opt}")
        answer = input("Choose (1-4): ")

        if answer.isdigit() and int(answer) - 1 == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            correct = q['options'][q['answer']]
            print(f"❌ Wrong! The correct answer is: {correct}\n")

    print(f"🏁 Quiz finished! You scored {score}/{len(questions)} points.")
    print("\nThanks for playing 💖")

if __name__ == "__main__":
    try:
        questions = load_questions()
        run_quiz(questions)
    except FileNotFoundError:
        print("⚠️ The file 'questions.json' was not found! Please create it in the same folder.")
