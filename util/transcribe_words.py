from faster_whisper import WhisperModel


model = WhisperModel("base", device="cpu", compute_type="int8")


audio_path = "001.mp3"


segments, info = model.transcribe(audio_path, word_timestamps=True)

output_file = "transcription_output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for segment in segments:
        f.write(segment.text + "\n")
        for word in segment.words:
            f.write(f"[{word.start:.2f}s - {word.end:.2f}s] {word.word}\n")

print(f"✅ Transcription saved to: {output_file}")