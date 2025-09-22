from TTS.api import TTS
import os
import torch

print("Loading model...")
device = "mps" if torch.backends.mps.is_available() else "cpu"
device = "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
print("Device:", device)
print("Speakers:", tts.speakers)
print("Languages:", tts.languages)
os.makedirs("output", exist_ok=True)


def process(text, lang, voice):
    tts.tts_to_file(
        file_path=f"output/coqui_xtts_{lang}.wav",
        text=text,
        language=lang,
        speaker=voice,
    )
    print(f"Created output/coqui_xtts_{lang}.wav")


text = "A rainbow is a meteorological phenomenon that is caused by reflection, refraction and dispersion of light."
lang = "en"
voice = "Claribel Dervla"
process(text, lang, voice)

text = "Un arcoíris o arco iris es un fenómeno óptico y meteorológico que consiste en la aparición en el cielo de un arco de luz multicolor."  # Change to the text you want to generate
lang = "es"
voice = "Uta Obando"
process(text, lang, voice)
