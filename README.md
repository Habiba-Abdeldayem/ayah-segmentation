# 📖 Ayah Segmentation

Transcribes Quran recitation audio with word-level timestamps using `faster-whisper`.

---

## ⚙️ Setup

```bash
# 1. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate       # Windows
# source venv/bin/activate    # macOS/Linux

# 2. Install dependencies
pip install faster-whisper transformers librosa pydub soundfile rapidfuzz
```

---

## 🚀 Run

Place your audio file (e.g., `001.mp3`) and run:

```bash
python transcribe.py
```

Output will be saved to `transcription_output.txt`.

---

