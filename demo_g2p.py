import epitran
import g2p

# https://github.com/dmort27/epitran#installation-of-flite-for-english-g2p
# epi = epitran.Epitran("eng-Latn")
# print(epi.transliterate("Berkeley"))

epi = epitran.Epitran("spa-Latn")
print(epi.transliterate("meteorológico"))

epi = epitran.Epitran("tur-Latn")
print(epi.word_to_tuples("Düğün"))

# https://github.com/roedoejet/g2p
transducer = g2p.make_g2p("eng", "eng-ipa")
print(transducer("Berkeley"))
