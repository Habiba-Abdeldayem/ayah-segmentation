from faster_whisper import WhisperModel
from rapidfuzz import fuzz
import json

# Load model (use your custom or base one)
model = WhisperModel("base", device="cpu", compute_type="int8")
# model = WhisperModel("large-v3", device="cpu", compute_type="int8") #try this model later
# model = WhisperModel("OdyAsh/faster-whisper-base-ar-quran", device="cpu", compute_type="int8") #model with low accuracy


# Transcribe audio
segments, _ = model.transcribe("001.mp3", beam_size=5, word_timestamps=True, language="ar")

# Load Quran text
with open("quran-simple.json", "r", encoding="utf-8") as f:
    quran = json.load(f)

# Preprocess ayahs into list of (surah_ayah, text)
ayah_list = list(quran.items())

aligned_results = []

# Go through transcription segments
for segment in segments:
    seg_text = segment.text.strip()

    best_match = None
    best_score = 0

    for ayah_id, ayah_text in ayah_list:
        score = fuzz.token_set_ratio(seg_text, ayah_text)
        if score > best_score:
            best_score = score
            best_match = (ayah_id, ayah_text)

    # Save aligned ayah with segment time
    if best_match and best_score > 40:  # adjust threshold if needed
        aligned_results.append({
            "ayah": best_match[0],
            "text": best_match[1],
            "score": best_score,
            "start": segment.start,
            "end": segment.end
        })

# Save to file
with open("aligned_output.json", "w", encoding="utf-8") as f:
    json.dump(aligned_results, f, ensure_ascii=False, indent=2)

print("✅ Alignment complete.")
