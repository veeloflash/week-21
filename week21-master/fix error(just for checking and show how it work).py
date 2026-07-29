import os
import re

ROOT = "Week21_Engineering"

def fix_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    content = re.sub(
        r"from (.+?) import load_documents\b",
        r"from \1 import load_documents_from_json",
        content
    )

    content = re.sub(
        r"\bload_documents\(\)",
        r'load_documents_from_json("dataset.json")',
        content
    )

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"--Fixed: {path}")
    else:
        print(f"xxNo change: {path}")


def walk_and_fix(root):
    for folder, _, files in os.walk(root):
        for file in files:
            if file.endswith(".py"):
                fix_file(os.path.join(folder, file))


walk_and_fix(ROOT)
print("All files processed.")
