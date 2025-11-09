import json
import random
import os
from data import load_questions

HIGHSCORE_FILE = "highscores.json"

# --- Utility Functions ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_highscores():
    if not os.path.exists(HIGHSCORE_FILE):
        return []
    with open(HIGHSCORE_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_highscore(name, score):
    highscores = load_highscores()
    highscores.append({"name": name, "score": score})
    highscores = sorted(highscores, key=lambda x: x["score"], reverse=True)[:10]
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump(highscores, f, indent=4)

# --- Core Quiz Logic ---
def play_quiz():
    questions_data = load_questions()

    # Show available subjects
    print("\n📘 Choose a subject:")
    subjects = list(questions_data.keys())
    for i, subject in enumerate(subjects, 1):
        print(f"{i}. {subject}")

    try:
        choice = int(input("Enter your choice number: "))
        if choice < 1 or choice > len(subjects):
            print("❌ Invalid choice! Returning to menu.\n")
            return
    except ValueError:
        print("❌ Please enter a valid number!\n")
        return

    subject = subjects[choice - 1]
    questions = questions_data.get(subject, [])

    if not questions:
        print(f"⚠️ No questions found for {subject}.\n")
        return

    print(f"\n🎯 Starting Quiz: {subject}")
    print("=" * 45)

    # Pick exactly 5 questions (or all if <5)
    selected_questions = random.sample(questions, min(5, len(questions)))

    score = 0
    correct_answers = 0

    for idx, q in enumerate(selected_questions, 1):
        print(f"\nQuestion {idx}: {q['question']}")
        for i, option in enumerate(q['options'], 1):
            print(f"  {i}. {option}")

        try:
            ans = int(input("Your answer (1-4): "))
        except ValueError:
            print("❌ Invalid input! Skipping question.")
            continue

        if ans == q['answer']:
            print("✅ Correct!")
            score += 10
            correct_answers += 1
        else:
            correct_option = q['options'][q['answer'] - 1]
            print(f"❌ Wrong! Correct answer: {correct_option}")

    print("\n🏁 Quiz Finished!")
    print(f"🎓 You got {correct_answers}/{len(selected_questions)} correct!")
    print(f"💯 Final Score: {score}/{len(selected_questions) * 10} points")
    print("=" * 45)

    name = input("\nEnter your name for the leaderboard (or press Enter to skip): ").strip()
    if name:
        save_highscore(name, score)

    input("\nPress Enter to return to the main menu...")

# --- Leaderboard ---
def view_highscores():
    clear_screen()
    scores = load_highscores()
    print("\n🏆 Leaderboard:")
    print("=" * 40)
    if not scores:
        print("No highscores yet! Play a quiz to add your name.")
    else:
        for i, entry in enumerate(scores, 1):
            print(f"{i}. {entry['name']} — {entry['score']} points")
    print("=" * 40)
    input("\nPress Enter to return to menu...")

# --- Main Menu ---
def main_menu():
    while True:
        clear_screen()
        print("🎮 MAIN MENU")
        print("=" * 30)
        print("1. Play Quiz")
        print("2. View Highscores")
        print("3. Exit")
        print("=" * 30)

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            play_quiz()
        elif choice == "2":
            view_highscores()
        elif choice == "3":
            print("\n👋 Thanks for playing! See you soon!")
            break
        else:
            print("❌ Invalid choice! Try again.")
            input("Press Enter to continue...")

# --- Entry Point ---
if __name__ == "__main__":
    main_menu()
