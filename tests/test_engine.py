
import unittest

from nexus_core.engine import NexusEngine


class TestNexusEngine(unittest.TestCase):

    def setUp(self):
        self.engine = NexusEngine()

    def test_engine_status(self):
        result = self.engine.get_status()

        self.assertEqual(result["name"], "NEXUS IA")
        self.assertEqual(result["status"], "ready")
        self.assertFalse(result["ai_connected"])

    def test_process_message(self):
        result = self.engine.process("Olá NEXUS")

        self.assertTrue(result["success"])
        self.assertEqual(result["message"], "Olá NEXUS")
        self.assertEqual(result["mode"], "basic")

    def test_empty_message(self):
        result = self.engine.process("")

        self.assertFalse(result["success"])

    def test_invalid_message(self):
        result = self.engine.process(None)

        self.assertFalse(result["success"])

    def test_message_too_long(self):
        result = self.engine.process("A" * 4001)

        self.assertFalse(result["success"])


if __name__ == "__main__":
    unittest.main()
