quran_json = {}

with open("quran-simple.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("|")
        if len(parts) == 3:
            surah, ayah, text = parts
            key = f"{int(surah)}:{int(ayah)}"
            quran_json[key] = text

# Save as JSON
import json
with open("quran-simple.json", "w", encoding="utf-8") as f:
    json.dump(quran_json, f, ensure_ascii=False, indent=2)

print("✅ Saved as quran_text.json")
