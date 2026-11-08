
"""
NEXUS ENGINE
Motor central de processamento da NEXUS IA.
Preparado para integração futura com modelos de IA.
"""


class NexusEngine:

    def __init__(self, provider=None):
        self.name = "NEXUS IA"
        self.version = "0.2.0"
        self.status = "ready"
        self.provider = provider
        self.max_message_length = 4000

    def get_status(self):
        return {
            "name": self.name,
            "version": self.version,
            "status": self.status,
            "ai_connected": self.provider is not None
        }

    def process(self, message):

        if not isinstance(message, str):
            return {
                "success": False,
                "error": "A mensagem precisa ser um texto."
            }

        message = message.strip()

        if not message:
            return {
                "success": False,
                "error": "Mensagem vazia."
            }

        if len(message) > self.max_message_length:
            return {
                "success": False,
                "error": "A mensagem ultrapassou o limite permitido."
            }

        if self.provider is not None:
            try:
                response = self.provider.generate(message)

                if not isinstance(response, str) or not response.strip():
                    raise ValueError("Resposta inválida do provedor.")

                return {
                    "success": True,
                    "message": response.strip(),
                    "engine": self.name,
                    "mode": "ai"
                }

            except Exception:
                return {
                    "success": False,
                    "error": "Não foi possível processar a solicitação."
                }

        return {
            "success": True,
            "message": message,
            "engine": self.name,
            "mode": "basic"
        }


nexus_engine = NexusEngine()
