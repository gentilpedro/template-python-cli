"""Domain layer: pure business rules, no I/O, no framework dependencies."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Greeting:
    recipient: str

    def __post_init__(self) -> None:
        if not self.recipient.strip():
            raise ValueError("recipient must not be empty")

    def message(self) -> str:
        return f"Hello, {self.recipient}!"
