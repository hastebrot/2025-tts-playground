from kokoro import KPipeline, KModel
import soundfile as sf
import torch

print("Loading model...")
device = "mps" if torch.backends.mps.is_available() else "cpu"
device = "cpu"
model = KModel(repo_id="hexgrad/Kokoro-82M").to(device).eval()


def process(text, lang, voice):
    lang_code = "b" if lang == "en-gb" else "a" if lang == "en-us" else lang
    pipeline = KPipeline(repo_id="hexgrad/Kokoro-82M", model=model, lang_code=lang_code)
    phonemes, tokens = pipeline.g2p(text)
    print("Phonemes:", phonemes)
    print("Tokens:", len(tokens) if tokens else 0)

    generator = pipeline(
        text,
        voice=voice,
        speed=1.0,
        split_pattern=r"\n+",
    )
    # generator = pipeline.generate_from_tokens(tokens=phonemes, voice=voice, speed=1.0)
    for index, result in enumerate(generator):
        gs = result.graphemes
        ps = result.phonemes
        ts = result.tokens
        print(lang, index, gs, ps)
        if ts:
            for t in ts:
                print(t.text, repr(t.whitespace), t.start_ts, t.end_ts)
        sf.write(f"output/kokoro_{lang}_{index}.wav", result.audio, 24000)
        print(f"Created output/kokoro_{lang}_{index}.wav")


text = "A rainbow is a meteorological phenomenon that is caused by reflection, refraction and dispersion of light."
lang = "en-gb"
voice = "bf_emma"
process(text, lang, voice)

text = "Un arcoíris o arco iris es un fenómeno óptico y meteorológico que consiste en la aparición en el cielo de un arco de luz multicolor."
lang = "es"
voice = "em_alex"
process(text, lang, voice)
