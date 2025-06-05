import google.generativeai as genai
import json
import os
from datetime import datetime
from py2neo import Graph, Node, Relationship

# --- CONFIG ---
genai.configure(api_key="YOUR_GEMINI_API_KEY")
graph = Graph("bolt://localhost:7687", auth=("neo4j", "Thatha@123"))

# --- MEMORY FILES ---
def load_memory(story_name):
    filename = f"memory_{story_name}.json"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def save_memory(story_name, memory):
    filename = f"memory_{story_name}.json"
    with open(filename, "w") as file:
        json.dump(memory, file, indent=4)

def get_relevant_memory(memory, limit=5):
    return "\n".join([f"User: {m['user']}\nChatbot: {m['chatbot']}" for m in memory[-limit:]])

# --- NEO4J INTEGRATION ---
def save_scene_to_neo4j(story_name, user_input, chatbot_reply):
    timestamp = str(datetime.now())
    scene = Node("Scene", text=chatbot_reply, user_input=user_input, timestamp=timestamp)

    story = graph.nodes.match("Story", title=story_name).first()
    if not story:
        story = Node("Story", title=story_name, created_at=timestamp)
        graph.create(story)

    rel = Relationship(scene, "PART_OF", story)
    graph.create(scene | rel)

# --- CHATBOT SETUP ---
story_name = input("Which story are you working on? ").strip()
chat_memory = load_memory(story_name)
model = genai.GenerativeModel("gemini-1.5-pro-002")

print(f"\n🧠 Chatbot initialized for story: {story_name}")
print("Type 'switch to [story]' to change stories, or 'exit' to leave.\n")

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
        print(f"\n🔁 Switched to story: {story_name}\n")
        continue

    # Use previous memory for context
    past_context = get_relevant_memory(chat_memory, limit=5)
    full_prompt = f"Memory:\n{past_context}\nUser: {user_input}\nChatbot:"

    response = model.generate_content(full_prompt)
    chatbot_reply = response.text if hasattr(response, "text") else response.candidates[0].content.parts[0].text

    chat_memory.append({
        "timestamp": str(datetime.now()),
        "user": user_input,
        "chatbot": chatbot_reply
    })

    save_memory(story_name, chat_memory)
    save_scene_to_neo4j(story_name, user_input, chatbot_reply)

    print("Chatbot:", chatbot_reply, "\n\n")
