import openai
import os
import json

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Memory storage file
MEMORY_FILE = "memory.json"

# Load existing memory if available
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory_lanes = json.load(f)
else:
    memory_lanes = {}

def chat_with_ai(user_input, story_name):
    """
    Handles conversation with AI, storing memory separately for different stories.
    """
    if story_name not in memory_lanes:
        memory_lanes[story_name] = []  # Create new memory lane for a story

    # Add user input to memory
    memory_lanes[story_name].append({"role": "user", "content": user_input})

    # Call OpenAI API
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=memory_lanes[story_name]  # Uses stored conversation history
    )

    reply = response.choices[0].message.content  # Extract AI response
    memory_lanes[story_name].append({"role": "assistant", "content": reply})

    # Save updated memory
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory_lanes, f, indent=4)

    return reply

if __name__ == "__main__":
    print("AI Storyteller - Type 'exit' to stop.")
    story_name = input("Enter story name: ")  # Ask for a story memory lane

    while True:
        user_input = input(f"You ({story_name}): ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("AI:", chat_with_ai(user_input, story_name))
