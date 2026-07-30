import os
import json
from pathlib import Path

locales_dir = Path(__file__).parent.parent / "app" / "frontend" / "src" / "locales"

if locales_dir.exists():
    for locale_folder in locales_dir.iterdir():
        if locale_folder.is_dir():
            translation_file = locale_folder / "translation.json"
            if translation_file.exists():
                with open(translation_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                data["pageTitle"] = "VectorCraft AI"
                data["headerTitle"] = "VectorCraft AI"
                
                with open(translation_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                    f.write("\n")
                print(f"Updated {translation_file.name} in {locale_folder.name}")
