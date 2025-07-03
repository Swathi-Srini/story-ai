from memory_manager import load_memory, save_memory, get_relevant_memory
from neo4j_manager import save_scene
from llm_manager import get_chatbot_reply

print("📌 AI Story Chat Initialized")
story_name = input("Which story are you working on? ").strip()
chat_memory = load_memory(story_name)

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

    past_context = get_relevant_memory(chat_memory, limit=5)
    full_prompt = f"Memory:\n{past_context}\nUser: {user_input}\nChatbot:"

    chatbot_reply = get_chatbot_reply(full_prompt)

    chat_memory.append({
        "user": user_input,
        "chatbot": chatbot_reply
    })

    save_memory(story_name, chat_memory)
    save_scene(story_name, user_input, chatbot_reply)

    print("Chatbot:", chatbot_reply, "\n")
