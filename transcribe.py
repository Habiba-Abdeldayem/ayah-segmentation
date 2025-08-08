# transcribe.py

from faster_whisper import WhisperModel

# Load the Quran-specific Arabic Whisper model
model = WhisperModel("OdyAsh/faster-whisper-base-ar-quran", device="cpu", compute_type="int8")

# Transcribe the recitation
segments, info = model.transcribe("001.mp3", beam_size=5, word_timestamps=True)

# Save word-level results
with open("transcription.txt", "w", encoding="utf-8") as f:
    for segment in segments:
        print(f"[{segment.start:.2f}s - {segment.end:.2f}s] {segment.text}")
        f.write(f"[{segment.start:.2f}s - {segment.end:.2f}s] {segment.text}\n")
