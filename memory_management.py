import json
import os

def load_memory(story_name):
    filename = f"memory/{story_name}.json"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def save_memory(story_name, memory):
    filename = f"memory/{story_name}.json"
    with open(filename, "w") as file:
        json.dump(memory, file, indent=4)

def get_relevant_memory(memory, limit=5):
    return "\n".join([f"User: {m['user']}\nChatbot: {m['chatbot']}" for m in memory[-limit:]])
