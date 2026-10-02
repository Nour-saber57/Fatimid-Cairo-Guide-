import os

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google import genai

router = APIRouter()


def get_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY is not configured. Set it before calling /chat."
        )
    return genai.Client(api_key=api_key)


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):
    client = get_client()

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=request.message
    )

    return {
        "response": response.output_text
    }