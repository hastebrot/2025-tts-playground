# 2025-tts-playground

- `❯ curl -LsSf https://astral.sh/uv/install.sh | sh`
- `❯ git clone https://github.com/hastebrot/2025-tts-playground`
- `❯ cd 2025-tts-playground/`
- `❯ uv run python hello.py`

## entry points

coqui:
- `❯ uv run python demo_coqui_xtts.py`

kokoro:
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

- https://github.com/hexgrad/kokoro
- https://huggingface.co/hexgrad/Kokoro-82M
- https://github.com/hexgrad/misaki
- https://github.com/Troyanovsky/awesome-TTS-Colab/tree/main
- https://github.com/adrianlyjak/kokoro-onnx-export
- https://github.com/hexgrad/kokoro/blob/2dd9df67793b635bb4f7228608c35ab09da9ee3f/kokoro/pipeline.py#L276C4-L276C83
- https://github.com/hexgrad/kokoro/issues/32
- https://github.com/Microsoft/onnxruntime
- MToken: https://github.com/hexgrad/misaki/blob/34552e03a2855cf1ab531ba2c9c3fdd89ed84432/misaki/en.py#L15
- https://github.com/KoljaB/RealtimeTTS/issues/278#issuecomment-2733161012
