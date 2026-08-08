"""Application configuration loaded from environment variables (.env)."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"


def _load_dotenv(path: Path) -> None:
    """Minimal stdlib-only .env loader (KEY=VALUE per line, # comments).

    Keeps the template dependency-free out of the box. Swap for
    python-dotenv if your project already depends on it.
    """
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


_load_dotenv(BASE_DIR / ".env")


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "template-python-cli")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    output_dir: Path = OUTPUT_DIR


settings = Settings()
