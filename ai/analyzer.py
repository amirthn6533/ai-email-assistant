from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze_email(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"""
Analyze this email and return:

1. Importance (Important or Not Important)
2. A short summary
3. A professional reply

Email:
{text}
"""
            }
        ]
    )

    return {
        "text": text,
        "analysis": response.choices[0].message.content.strip()
    }