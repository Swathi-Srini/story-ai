import google.generativeai as genai

genai.configure(api_key="AIzaSyDhG35ePgrtWSEUYuR_k3i2JclhXPgN5vU")

for model in genai.list_models():
    print(model.name)
