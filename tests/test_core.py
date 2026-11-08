import unittest

from nexus_core.core import nexus_core


class TestNexusCore(unittest.TestCase):

    def test_status(self):
        result = nexus_core.status()

        self.assertEqual(result["system"], "NEXUS IA")
        self.assertEqual(result["status"], "online")

    def test_process_message(self):
        result = nexus_core.process("Olá NEXUS")

        self.assertTrue(result["success"])
        self.assertEqual(result["message"], "Olá NEXUS")

    def test_empty_message(self):
        result = nexus_core.process("")

        self.assertFalse(result["success"])


if __name__ == "__main__":
    unittest.main()
