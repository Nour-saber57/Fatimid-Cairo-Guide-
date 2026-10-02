import os
import importlib
import unittest


class ChatRouterImportTest(unittest.TestCase):
    def test_chat_router_imports_without_api_key(self):
        os.environ.pop("GEMINI_API_KEY", None)
        import routers.chat as chat_module
        self.assertTrue(hasattr(chat_module, "router"))
        self.assertTrue(callable(chat_module.chat))


if __name__ == "__main__":
    unittest.main()
