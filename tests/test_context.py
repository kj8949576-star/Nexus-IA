
import unittest

from nexus_core.context import NexusContext


class TestNexusContext(unittest.TestCase):

    def setUp(self):
        self.context = NexusContext(max_messages=3)

    def test_add_message(self):
        result = self.context.add_message("user", "Olá NEXUS")

        self.assertTrue(result)
        self.assertEqual(len(self.context.get_context()), 1)

    def test_reject_empty_message(self):
        result = self.context.add_message("user", "")

        self.assertFalse(result)

    def test_reject_invalid_role(self):
        result = self.context.add_message("", "Olá")

        self.assertFalse(result)

    def test_message_limit(self):
        self.context.add_message("user", "Mensagem 1")
        self.context.add_message("user", "Mensagem 2")
        self.context.add_message("user", "Mensagem 3")
        self.context.add_message("user", "Mensagem 4")

        messages = self.context.get_context()

        self.assertEqual(len(messages), 3)
        self.assertEqual(messages[0]["content"], "Mensagem 2")

    def test_clear_context(self):
        self.context.add_message("user", "Olá")

        self.context.clear()

        self.assertEqual(len(self.context.get_context()), 0)

    def test_status(self):
        result = self.context.get_status()

        self.assertEqual(result["status"], "ready")
        self.assertEqual(result["max_messages"], 3)


if __name__ == "__main__":
    unittest.main()
