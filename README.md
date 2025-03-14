# AI Storytelling Chatbot

An interactive chatbot that helps you write and manage multiple stories while keeping track of past conversations. The bot remembers story details, allowing seamless storytelling across different projects.

## Features

✅ **Multi-Story Support** – Work on multiple stories without mixing their details. Switch between stories anytime.
✅ **Persistent Memory** – Saves past conversations and reloads them when you continue a story.
✅ **Context Awareness** – Uses past messages to generate relevant and consistent responses.
✅ **Smart Memory Retrieval** – Retrieves only the most relevant past messages to keep responses focused.
✅ **Story Switching** – Easily switch between different projects while keeping memories intact.
✅ **JSON-Based Memory Storage** – Each story has its own memory file (`memory_[story_name].json`).

---

## Installation

### Prerequisites
- Python 3.x
- Google Gemini AI API Key (replace `YOUR_API_KEY` in the script)

### Setup
1. **Clone the repository**:
   ```sh
   git clone https://github.com/YOUR_USERNAME/AI-Storytelling-Chatbot.git
   cd AI-Storytelling-Chatbot
   ```

2. **Install dependencies**:
   ```sh
   pip install google-generativeai
   ```

3. **Set up your API key**:
   Open `main.py` and replace:
   ```python
   genai.configure(api_key="YOUR_API_KEY")
   ```
   with your actual API key.

4. **Run the chatbot**:
   ```sh
   python main.py
   ```

---

## Usage

1. **Start the chatbot** and enter the name of the story you’re working on.
2. **Chat naturally** – The bot will remember past messages and continue the story.
3. **Switch stories** anytime by typing:
   ```
   switch to [story_name]
   ```
4. **Exit** by typing `exit`, `quit`, or `bye`. The chatbot will save your story progress.

---

## File Structure

AI-Storytelling-Chatbot/
│── main.py              # Main chatbot script
│── memory_*.json        # Story memory files (generated per story)
│── README.md            # Documentation


---

## Future Improvements
- **Long-Term Story Summarization** – Summarize older messages to save space.
- **Better Context Retrieval** – Use AI embeddings to find the most relevant past messages.
- **Character & Plot Tracking** – Store key events and character details for consistency.

Contributions & suggestions are welcome! 🚀

