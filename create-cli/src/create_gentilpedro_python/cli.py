import argparse
import shutil
import sys
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "template"
PLACEHOLDER = "template-python-cli"
RENAME_FILES = ("template.spec", "build_app.py")


def main() -> None:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(prog="create-gentilpedro-python")
    parser.add_argument("name", nargs="?", help="Nome do projeto/pasta")
    args = parser.parse_args()

    name = args.name or input("Nome do projeto: (meu-projeto-python) ").strip() or "meu-projeto-python"

    target = Path.cwd() / name
    if target.exists() and any(target.iterdir()):
        print(f'Erro: a pasta "{name}" já existe e não está vazia.', file=sys.stderr)
        sys.exit(1)

    shutil.copytree(TEMPLATE_DIR, target)

    for relative in RENAME_FILES:
        f = target / relative
        if f.exists():
            f.write_text(f.read_text(encoding="utf-8").replace(PLACEHOLDER, name), encoding="utf-8")

    print(f"\nProjeto criado em ./{name}\n")
    print("Próximos passos:")
    print(f"  cd {name}")
    print("  python -m venv .venv")
    print("  .venv\\Scripts\\activate       (Windows)  ou  source .venv/bin/activate  (Linux/Mac)")
    print("  pip install -r requirements.txt")
    print("  python main.py --hello Mundo\n")


if __name__ == "__main__":
    main()
