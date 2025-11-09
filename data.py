import json
import os

def load_questions():
    path = 'questions.json'
    if not os.path.exists(path):
        print("❌ questions.json not found in project folder!")
        return {}
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("❌ Invalid JSON format in questions.json!")
        return {}
