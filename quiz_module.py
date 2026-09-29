import google.generativeai as genai

def generate_quiz(topic):
    prompt = f"Create 5 simple multiple-choice questions about {topic}, with answers."
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
