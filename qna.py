import google.generativeai as genai


def answer_question(question):
    prompt = f"""
    Answer this question clearly and simply:
    {question}
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text
