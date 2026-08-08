"""Builds a standalone executable with PyInstaller.

Usage:
    python build_app.py

Produces dist/template-python-cli(.exe). Requires PyInstaller
(see requirements-dev.txt). Rename APP_NAME below when you rename the project.
"""
import PyInstaller.__main__

APP_NAME = "template-python-cli"

PyInstaller.__main__.run(
    [
        "main.py",
        f"--name={APP_NAME}",
        "--onefile",
        "--clean",
        "--noconfirm",
    ]
)
