import google.generativeai as genai


def explain_topic(topic):
    prompt = f"""
    Explain the following topic in simple and easy language:
    {topic}

    Give a clear and beginner-friendly explanation.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text
