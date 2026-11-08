
"""
NEXUS IA - CORE
Núcleo principal do sistema.
"""

from nexus_core.engine import NexusEngine


class NexusCore:

    def __init__(self):
        self.name = "NEXUS IA"
        self.version = "0.2.0"
        self.status_value = "online"
        self.engine = NexusEngine()

    def status(self):
        return {
            "system": self.name,
            "version": self.version,
            "status": self.status_value,
            "engine": self.engine.get_status()
        }

    def process(self, message):
        return self.engine.process(message)

    def get_engine(self):
        return self.engine.get_status()


nexus_core = NexusCore()
