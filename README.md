# 2025-tts-playground

- `❯ curl -LsSf https://astral.sh/uv/install.sh | sh`
- `❯ git clone https://github.com/hastebrot/2025-tts-playground`
- `❯ cd 2025-tts-playground/`
- `❯ uv run python hello.py`

## entry points

coqui:
- `❯ uv run python demo_coqui_xtts.py`

kokoro:
- `❯ PYTORCH_ENABLE_MPS_FALLBACK=1 uv run python demo_kokoro.py`
- `❯ uv run python demo_kokoro.py`
- `❯ uv run python demo_kokoro_ts.py`

kokoro with onnx:
- `❯ wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx`
- `❯ wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin`
- `❯ uv run python demo_onnx_kokoro.py`

## dependencies

- `"coqui-tts==0.26.1"`
- `"kokoro==0.9.4"`
- `"kokoro-onnx>=0.4.9"`
- `"pip>=25.2"`
- `"ruff>=0.13.1"`
- `"soundfile>=0.13.1"`

## cheatsheet

```sh
❯ uv init
Initialized project `2025-tts-playground`
```

- `❯ uv python pin 3.13`
- `❯ uv python install`
- `❯ uv init -p 3.13`
- `❯ uv run python hello.py`
- `❯ uv add "coqui-tts==0.26.1"`

## links

tts:
- https://github.com/Troyanovsky/awesome-TTS-Colab/tree/main
- https://github.com/KoljaB/RealtimeTTS/issues/278#issuecomment-2733161012

espeak-ng:
> espeak-ng is a Text-to-Speech software supporting a lot of languages and IPA (International Phonetic Alphabet) output.
- https://github.com/espeak-ng/espeak-ng
- https://github.com/bootphon/phonemizer

g2p:
> Grapheme-to-Phoneme transductions that preserve input and output indices, and support cross-lingual g2p! 
- https://github.com/roedoejet/g2p
- Pine, et al (2022): "Gi2Pi Rule-based, index-preserving grapheme-to-phoneme transformations"
- https://github.com/dmort27/epitran

gruut:
> A tokenizer, text cleaner, and phonemizer for many human languages.
- https://github.com/rhasspy/gruut

kokoro:
- https://github.com/hexgrad/kokoro
- https://huggingface.co/hexgrad/Kokoro-82M
- https://github.com/hexgrad/kokoro/blob/2dd9df67793b635bb4f7228608c35ab09da9ee3f/kokoro/pipeline.py#L276C4-L276C83
- https://github.com/hexgrad/kokoro/issues/32
- https://github.com/hexgrad/misaki
- MToken: https://github.com/hexgrad/misaki/blob/34552e03a2855cf1ab531ba2c9c3fdd89ed84432/misaki/en.py#L15

kokoro for onnx:
- https://github.com/Microsoft/onnxruntime
- https://github.com/adrianlyjak/kokoro-onnx-export

whisper:
> faster-whisper is a reimplementation of OpenAI's Whisper model using CTranslate2, which is a fast inference engine for Transformer models. 
- https://github.com/AIXerum/faster-whisper
- https://github.com/NeuralFalconYT/Whisper-Turbo-Subtitle

forced alignment:
> aeneas automatically generates a synchronization map between a list of text fragments and an audio file containing the narration of the text. In computer science this task is known as (automatically computing a) forced alignment.
- https://github.com/topics/forced-alignment
- https://github.com/readbeyond/aeneas

kitten tts:
- https://github.com/KittenML/KittenTTS
- https://huggingface.co/KittenML/kitten-tts-nano-0.2
- https://news.ycombinator.com/item?id=44807868

text-to-speach unified interface:
- https://github.com/willwade/tts-wrapper
