import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
REPO_ROOT = HERE.parent
TEMPLATE_DIR = HERE / "src" / "create_gentilpedro_python" / "template"

EXCLUDE_TOP_LEVEL = {".github", "create-cli"}

shutil.rmtree(TEMPLATE_DIR, ignore_errors=True)
TEMPLATE_DIR.mkdir(parents=True)

files = subprocess.run(
    ["git", "ls-files"], cwd=REPO_ROOT, capture_output=True, text=True, check=True
).stdout.splitlines()

count = 0
for rel in files:
    if not rel or rel.split("/", 1)[0] in EXCLUDE_TOP_LEVEL:
        continue
    src = REPO_ROOT / rel
    dest = TEMPLATE_DIR / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    count += 1

print(f"Synced {count} files into create-cli/src/create_gentilpedro_python/template/")
