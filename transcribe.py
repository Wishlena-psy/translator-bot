#!/usr/bin/env python3
"""Расшифровка аудио для translator-bot.

Вызов: transcribe.py <wav> [model] [lang]
  model — small (по умолчанию) / medium / large-v3
  lang  — код языка; если не задан, whisper определяет сам
          (это важно: собеседник говорит на своём языке,
           жёсткая подсказка ломала распознавание)
"""
import sys
import warnings

warnings.filterwarnings("ignore")

from faster_whisper import WhisperModel

audio_file = sys.argv[1]
model_size = sys.argv[2] if len(sys.argv) > 2 else "small"
lang = sys.argv[3] if len(sys.argv) > 3 else None

model = WhisperModel(model_size, device="cpu", compute_type="int8")
segments, info = model.transcribe(
    audio_file,
    language=lang,
    beam_size=5,
    vad_filter=True,                       # режем тишину: длинные диктофонные записи
    vad_parameters={"min_silence_duration_ms": 500},
)

text = " ".join(s.text for s in segments).strip()
print(text)
