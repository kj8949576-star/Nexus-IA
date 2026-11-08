
"""
NEXUS CONTEXT ENGINE
Gerenciamento do contexto das conversas.
"""


class NexusContext:

    def __init__(self, max_messages=20):
        self.max_messages = max_messages
        self.messages = []

    def add_message(self, role, content):

        if not isinstance(role, str) or not role.strip():
            return False

        if not isinstance(content, str) or not content.strip():
            return False

        message = {
            "role": role.strip(),
            "content": content.strip()
        }

        self.messages.append(message)

        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

        return True

    def get_context(self):
        return list(self.messages)

    def clear(self):
        self.messages.clear()
        return True

    def get_status(self):
        return {
            "total_messages": len(self.messages),
            "max_messages": self.max_messages,
            "status": "ready"
        }
