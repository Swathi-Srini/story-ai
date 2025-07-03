import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-pro-002")

def get_chatbot_reply(prompt):
    response = model.generate_content(prompt)
    return response.text if hasattr(response, "text") else response.candidates[0].content.parts[0].text
