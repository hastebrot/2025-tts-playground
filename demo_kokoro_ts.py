from dataclasses import dataclass
from typing import Optional
from kokoro import KModel, KPipeline
import numpy as np
import soundfile as sf
import torch

print("Loading model...")
device = "mps" if torch.backends.mps.is_available() else "cpu"
device = "cpu"
model = KModel(repo_id="hexgrad/Kokoro-82M").to(device).eval()


@dataclass
class MToken:
    text: str
    whitespace: str
    phonemes: Optional[str] = None
    start_ts: Optional[float] = None
    end_ts: Optional[float] = None


def process(text, lang, voice):
    lang_code = "b" if lang == "en-gb" else "a" if lang == "en-us" else lang
    pipeline = KPipeline(repo_id="hexgrad/Kokoro-82M", model=model, lang_code=lang_code)

    phonemes, tokens = pipeline.g2p(text)
    if tokens is None:
        tokens = []
        generator = pipeline(text, voice=voice, split_pattern=r"\s+")
        for result in generator:
            tokens.append(
                MToken(
                    text=result.graphemes,
                    phonemes=result.phonemes,
                    whitespace=" " if result.graphemes[-1].isalpha() else "",
                    start_ts=None,
                    end_ts=None,
                )
            )
        print(tokens)
    print("Phonemes:", phonemes)
    print("Tokens:", tokens)

    pack = pipeline.load_voice(voice).to(model.device)
    output = KPipeline.infer(model, phonemes, pack, speed=1.0)  # type: ignore
    if output.pred_dur is None:
        raise Exception("output.pred_dur is None")
    KPipeline.join_timestamps(tokens, output.pred_dur)

    for token in tokens:
        print(
            token.start_ts,
            token.end_ts,
            token.text,
            token.phonemes,
            repr(token.whitespace),
        )

    generator = pipeline(text, voice=voice)
    samples = []
    for index, result in enumerate(generator):
        # print(index, result.graphemes, result.phonemes, result.tokens)
        samples.append(result.audio)
    samples = np.concatenate(samples)
    sf.write(f"output/kokoro_ts_{lang}.wav", samples, 24000)


text = "A rainbow is a meteorological phenomenon that is caused by reflection, refraction and dispersion of light."
lang = "en-gb"
voice = "bf_emma"
process(text, lang, voice)

text = "Un arcoíris o arco iris es un fenómeno óptico y meteorológico que consiste en la aparición en el cielo de un arco de luz multicolor."
lang = "es"
voice = "em_alex"
process(text, lang, voice)
