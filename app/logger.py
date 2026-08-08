"""Central logging setup: console + rotating file, mirroring the Serilog
console+file pattern used in the .NET API templates."""
from __future__ import annotations

import logging
import sys
from logging.handlers import RotatingFileHandler

from app.config import settings


def setup_logging() -> logging.Logger:
    settings.output_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(settings.app_name)
    logger.setLevel(settings.log_level)

    if logger.handlers:
        return logger

    fmt = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(fmt)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        settings.output_dir / "app.log",
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    return logger


log = setup_logging()
