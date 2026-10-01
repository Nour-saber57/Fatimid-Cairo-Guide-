from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os

app = FastAPI()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(request: ChatRequest):

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=request.message
    )

    return {
        "response": response.output_text
    }