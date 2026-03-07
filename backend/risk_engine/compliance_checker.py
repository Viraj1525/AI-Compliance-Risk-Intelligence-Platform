from dotenv import load_dotenv
import os
from groq import Groq
from config.settings import MODEL_NAME

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_compliance(context):

    prompt = f"""
You are a compliance risk analyst.

Analyze the following company policy text and identify:

Risk:
Section:
Issue:
Severity:
Recommendation:

Document Text:
{context}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content