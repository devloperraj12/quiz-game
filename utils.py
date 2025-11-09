import json
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_highscores():
    if not os.path.exists('highscores.json'):
        return []
    with open('highscores.json', 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_highscore(name, category, score):
    scores = load_highscores()
    scores.append({"name": name, "category": category, "score": score})
    with open('highscores.json', 'w') as f:
        json.dump(scores, f, indent=4)
