"""
NEXUS IA - API
Interface de comunicação do sistema.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from nexus_core.core import nexus_core


app = FastAPI(
    title="NEXUS API",
    description="API oficial da NEXUS IA",
    version="0.1.0"
)


class MessageRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "system": "NEXUS IA",
        "api": "NEXUS API",
        "status": "online",
        "version": "0.1.0"
    }


@app.get("/status")
def status():
    return nexus_core.status()


@app.post("/process")
def process_message(request: MessageRequest):
    if not request.message.strip():
        raise HTTPException(
            status_code=400,
            detail="A mensagem não pode estar vazia."
        )

    return nexus_core.process(request.message)
