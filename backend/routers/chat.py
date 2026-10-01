import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto"
)

MODEL = "google/gemma-4-E4B-it"


def ask_gemma(question: str):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
You are the AI tour guide for Fatimid Cairo Guide.

Your job is to help visitors understand:
- Fatimid Cairo
- Islamic architecture
- Historic Cairo
- Fatimid monuments
- Mosques
- Gates
- Streets
- Historical events
- Cultural heritage

Answer clearly and accurately.
Do not invent historical facts.
If you are not sure about something, say so.
"""
            },
            {
                "role": "user",
                "content": question
            }
        ],
        max_tokens=500,
        temperature=0.7
    )

    return response.choices[0].message.content