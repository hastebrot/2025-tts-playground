import soundfile as sf
from misaki.espeak import EspeakG2P
from kokoro_onnx import Kokoro
from kokoro_onnx.tokenizer import Tokenizer

# import onnxruntime as ort
# print(ort.get_available_providers())

print("Loading model...")
kokoro = Kokoro("data/kokoro-v1.0.onnx", "data/voices-v1.0.bin")


def process(text, lang, voice):
    tokenizer = Tokenizer()
    phonemes = tokenizer.phonemize(text, lang=lang)
    tokens = tokenizer.tokenize(phonemes)
    print("Phonemes:", phonemes)
    # print("Tokens:", tokens)

    g2p = EspeakG2P(language=lang)
    phonemes, tokens = g2p(text)
    print("Phonemes:", phonemes)
    # print("Tokens:", tokens)

    samples, sample_rate = kokoro.create(phonemes, voice, is_phonemes=True)
    sf.write(f"output/onnx_kokoro_{lang}.wav", samples, sample_rate)
    print(f"Created output/onnx_kokoro_{lang}.wav")


text = "A rainbow is a meteorological phenomenon that is caused by reflection, refraction and dispersion of light."
lang = "en-gb"
voice = "bf_emma"
process(text, lang, voice)

text = "Un arcoíris o arco iris es un fenómeno óptico y meteorológico que consiste en la aparición en el cielo de un arco de luz multicolor."
lang = "es"
voice = "em_alex"
process(text, lang, voice)
