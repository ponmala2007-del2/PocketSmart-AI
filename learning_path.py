import google.generativeai as genai

def create_learning_path(topic):
    prompt = f"Create a simple step-by-step learning path for {topic}."
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
