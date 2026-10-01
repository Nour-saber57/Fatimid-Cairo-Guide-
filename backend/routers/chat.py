import os
from typing import Literal

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field


router = APIRouter()
CHAT_COMPLETIONS_URL = "https://router.huggingface.co/v1/chat/completions"
DEFAULT_MODEL = "Qwen/Qwen2.5-7B-Instruct"


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(min_length=1, max_length=2000)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    language: Literal["en", "ar"] = "en"
    place_context: str = Field(default="", max_length=6000)
    history: list[ChatMessage] = Field(default_factory=list, max_length=8)


class ChatResponse(BaseModel):
    answer: str


@router.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest) -> ChatResponse:
    token = os.getenv("HF_TOKEN")
    if not token:
        raise HTTPException(
            status_code=503,
            detail="The guide is not configured. Set HF_TOKEN on the backend.",
        )

    language_name = "Arabic" if payload.language == "ar" else "English"
    system_prompt = (
        "You are a careful historical guide to Al-Muizz Street and Fatimid Cairo. "
        f"Reply in {language_name}. Be concise, welcoming, and distinguish documented facts "
        "from uncertainty. Do not invent specific historical details. Use the selected "
        "monument notes when relevant; if the notes do not answer the question, say so."
    )
    if payload.place_context:
        system_prompt += f"\n\nSelected monument notes:\n{payload.place_context}"

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(message.model_dump() for message in payload.history)
    messages.append({"role": "user", "content": payload.message.strip()})

    try:
        async with httpx.AsyncClient(timeout=45) as client:
            response = await client.post(
                CHAT_COMPLETIONS_URL,
                headers={"Authorization": f"Bearer {token}"},
                json={
                    "model": os.getenv("HF_MODEL", DEFAULT_MODEL),
                    "messages": messages,
                    "max_tokens": 500,
                    "temperature": 0.4,
                },
            )
            response.raise_for_status()
    except httpx.TimeoutException as error:
        raise HTTPException(
            status_code=504,
            detail="The historical guide timed out. Please try again.",
        ) from error
    except httpx.HTTPStatusError as error:
        status_code = 503 if error.response.status_code == 429 else 502
        raise HTTPException(
            status_code=status_code,
            detail="The model provider rejected the request. Check HF_TOKEN and HF_MODEL.",
        ) from error
    except httpx.HTTPError as error:
        raise HTTPException(
            status_code=502,
            detail="The model provider could not be reached.",
        ) from error

    try:
        answer = response.json()["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError, ValueError) as error:
        raise HTTPException(
            status_code=502,
            detail="The model provider returned an unexpected response.",
        ) from error

    if not isinstance(answer, str) or not answer.strip():
        raise HTTPException(
            status_code=502,
            detail="The model provider returned an empty response.",
        )

    return ChatResponse(answer=answer.strip())