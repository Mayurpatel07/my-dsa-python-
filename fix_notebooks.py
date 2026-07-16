from pathlib import Path

fixed = 0

for file in Path(".").rglob("*.ipynb"):
    try:
        text = file.read_text(encoding="utf-8")

        # Find the last closing brace
        last = text.rfind("}")

        if last != -1 and last < len(text) - 1:
            extra = text[last + 1:].strip()

            if extra:
                file.write_text(text[:last + 1] + "\n", encoding="utf-8")
                print(f"✔ Fixed: {file}")
                fixed += 1

    except Exception as e:
        print(f"❌ Error: {file} -> {e}")

print(f"\nFinished! Fixed {fixed} notebook(s).")