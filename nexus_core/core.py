"""
NEXUS IA - CORE
Núcleo principal do sistema.
"""

from nexus_core.engine import NexusEngine


class NexusCore:

    def __init__(self):
        self.name = "NEXUS IA"
        self.version = "0.1.0"
        self.engine = NexusEngine()

    def status(self):
        return {
            "system": self.name,
            "version": self.version,
            "status": "online",
            "engine": self.engine.get_status()
        }

    def process(self, message):
        return self.engine.process(message)


nexus_core = NexusCore()
