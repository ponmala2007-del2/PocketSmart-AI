import google.generativeai as genai

def summarize_text(text):
    prompt = f"Summarize the following text in simple points:\n{text}"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
