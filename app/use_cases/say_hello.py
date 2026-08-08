"""Use case layer: orchestrates domain objects and infra, no I/O side effects
beyond what is explicitly delegated (e.g. logging)."""
from __future__ import annotations

from app.domain.greeting import Greeting
from app.logger import log


def say_hello(name: str) -> str:
    greeting = Greeting(recipient=name)
    message = greeting.message()
    log.info("Generated greeting for %s", name)
    return message
