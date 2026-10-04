import os
from pathlib import Path
from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from google import genai

router = APIRouter()
SYSTEM_INSTRUCTIONS_PATH = (
    Path(__file__).resolve().parents[1] / "tests" / "system-instructions.txt"
)


def get_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY is not configured. Set it before calling /chat."
        )
    return genai.Client(api_key=api_key)


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    message: str
    language: Literal["en", "ar"] = "en"
    place_context: str = ""
    history: list[ChatMessage] = Field(default_factory=list)


@router.post("/chat")
async def chat(request: ChatRequest):
    client = get_client()
    system_instruction = SYSTEM_INSTRUCTIONS_PATH.read_text(encoding="utf-8").strip()
    if request.place_context:
        system_instruction += f"\n\nCurrent monument reference:\n{request.place_context}"

    contents = [
        {
            "role": "model" if message.role == "assistant" else "user",
            "parts": [{"text": message.content}],
        }
        for message in request.history[-8:]
    ]
    contents.append({"role": "user", "parts": [{"text": request.message}]})

    try:
        response = await client.aio.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
            contents=contents,
            config={"system_instruction": system_instruction},
        )
    except Exception as error:
        print("========== GEMINI ERROR ==========")
        print(repr(error))
        print("===================================")

        raise HTTPException(
            status_code=502,
            detail=f"Gemini error: {str(error)}",
        ) from error

    return {"answer": response.text}