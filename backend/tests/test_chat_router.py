import os
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from routers.chat import ChatRequest, chat


class ChatRouterImportTest(unittest.TestCase):
    def test_chat_router_imports_without_api_key(self):
        os.environ.pop("GEMINI_API_KEY", None)
        import routers.chat as chat_module
        self.assertTrue(hasattr(chat_module, "router"))
        self.assertTrue(callable(chat_module.chat))


class GeminiChatTest(unittest.IsolatedAsyncioTestCase):
    async def test_chat_sends_context_and_history_and_returns_answer(self):
        generate_content = AsyncMock(return_value=SimpleNamespace(text="A historic answer."))
        client = SimpleNamespace(
            aio=SimpleNamespace(models=SimpleNamespace(generate_content=generate_content))
        )
        request = ChatRequest(
            message="When was it built?",
            language="ar",
            place_context="Monument: Al-Hakim Mosque",
            history=[
                {"role": "user", "content": "Tell me about this place."},
                {"role": "assistant", "content": "It is a Fatimid mosque."},
            ],
        )
        system_instruction = Path(__file__).with_name(
            "system-instructions.txt"
        ).read_text(encoding="utf-8").strip()

        with patch("routers.chat.get_client", return_value=client), patch.dict(
            os.environ, {"GEMINI_MODEL": "test-model"}
        ):
            result = await chat(request)

        self.assertEqual(result, {"answer": "A historic answer."})
        generate_content.assert_awaited_once_with(
            model="test-model",
            contents=[
                {"role": "user", "parts": [{"text": "Tell me about this place."}]},
                {"role": "model", "parts": [{"text": "It is a Fatimid mosque."}]},
                {"role": "user", "parts": [{"text": "When was it built?"}]},
            ],
            config={
                "system_instruction": (
                    f"{system_instruction}\n\n"
                    "Current monument reference:\nMonument: Al-Hakim Mosque"
                )
            },
        )


if __name__ == "__main__":
    unittest.main()
