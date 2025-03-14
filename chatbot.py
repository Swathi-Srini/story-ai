import google.generativeai as genai
import json
import os
from datetime import datetime

# Set up API key securely
genai.configure(api_key="YOUR_API_KEY_HERE")

# Function to load story memory
def load_memory(story_name):
    filename = f"memory_{story_name}.json"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []  # Start fresh if no memory exists

# Function to save story memory
def save_memory(story_name, memory):
    filename = f"memory_{story_name}.json"
    with open(filename, "w") as file:
        json.dump(memory, file, indent=4)

# Function to retrieve relevant past messages
def get_relevant_memory(memory, limit=5):
    return "\n".join([f"User: {m['user']}\nChatbot: {m['chatbot']}" for m in memory[-limit:]])

# Choose a story
story_name = input("Which story are you working on? ").strip()
chat_memory = load_memory(story_name)

# Select a valid model
model = genai.GenerativeModel("gemini-1.5-pro-002")

print(f"Chatbot initialized for story: {story_name}\nType 'switch to [story]' to change stories.")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        save_memory(story_name, chat_memory)
        break

    if user_input.lower().startswith("switch to "):
        save_memory(story_name, chat_memory)
        story_name = user_input[10:].strip()
        chat_memory = load_memory(story_name)
        print(f"Switched to story: {story_name}")
        continue

    # Retrieve past relevant messages
    past_context = get_relevant_memory(chat_memory, limit=5)
    full_prompt = f"Memory:\n{past_context}\nUser: {user_input}\nChatbot:"

    # Generate AI response
    response = model.generate_content(full_prompt)
    chatbot_reply = response.text if hasattr(response, "text") else response.candidates[0].content.parts[0].text

    # Store in memory with timestamps
    chat_memory.append({
        "timestamp": str(datetime.now()),
        "user": user_input,
        "chatbot": chatbot_reply
    })

    # Save memory
    save_memory(story_name, chat_memory)

    print("Chatbot:", chatbot_reply)
    print("")
