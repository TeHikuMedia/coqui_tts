class BaseEncoder:

    def encode(self, text):
        return text.replace('ng', 'ŋ').replace('wh', 'ƒ')

    def decode(self, text):
        return text.replace('ŋ', 'ng').replace('ƒ', 'wh')

class SingleVowel:

    encoder_dict = {
        'ā': 'aa',
        'ē': 'ee',
        'ī': 'ii',
        'ō': 'oo',
        'ū': 'uu',
        'ng': 'ŋ',
        'wh': 'ƒ'
    }

    decoder_dict = {v:k for k,v in encoder_dict.items()}

    def encode(self, text):
        for k, v in self.encoder_dict.items():
            text = text.replace(k, v)
        return text

    def decode(self, text):

        for k, v in self.decoder_dict.items():
            if k in text:
                text = text.replace(k, v)

        return text


# class Diphthong:

#     encoder_dict = {
#         'ae': 'æ',
#         'ai': 'á',
#         'ao': 'å',
#         'au': 'ä',
#         'ei': 'é',
#         'oe': 'œ',
#         'oi': 'ó',
#         'ou': 'ö',
#         'ng': 'ŋ',
#         'wh': 'ƒ',
#     }

#     decoder_dict = {v: k for k, v in encoder_dict.items()}

#     def tokenize(self, text, keep_spaces = False):
#         while len(text) > 0:
#             if keep_spaces and text[0] in [" ", "-"]:
#                 yield text[0]
#                 text = text[1:]
#             if text[0] in taumahi.orokati:
#                 yield text[0]
#                 text = text[1:]
#             elif text[0] in taumahi.oropuare:
#                 if len(text) > 1 and text[1] in taumahi.oropuare:
#                     if text[:2] in self.encoder_dict.keys():
#                         yield text[:2]
#                         text = text[2:]
#                     else:
#                         yield text[0]
#                         text = text[1:]
#                 else:
#                     yield text[0]
#                     text = text[1:]
#             else:
#                 text = text[1:]
#                 continue

#     def encode(self, text):
#         encoded_sents = []
#         for sent in text.split("\n"):
#             sent_encoded = []
#             for mora in self.tokenize(sent, keep_spaces = True):
#                 if mora in [" ", "-"]:
#                     sent_encoded.append(mora)
#                     continue
#                 try:
#                     if len(mora) > 1 or mora == "f":
#                         sent_encoded.append(self.encoder_dict[mora])
#                         continue
#                 except KeyError:
#                     log.error("KeyError: mora {} not in encoder_dict".format(mora))
#                 sent_encoded.append(mora)
#             text_encoded = ''.join(sent_encoded)
#             encoded_sents.append(text_encoded)
#         return '\n'.join(encoded_sents)

#     def decode(self, encoded_text):
#         for diphthong, mora in self.encoder_dict.items():
#              encoded_text = encoded_text.replace(mora, diphthong)
#         return encoded_text


# class Syllable:

#     encoder_dict = {
#         'a': 'ᅡ', 'h': 'ᄒ',
#         'ā': 'ᅣ', 'k': 'ᄏ',
#         'e': 'ᅦ', 'm': 'ᄆ',
#         'ē': 'ᅨ', 'n': 'ᄂ',
#         'i': 'ᅥ', 'p': 'ᄑ',
#         'ī': 'ᅧ', 'r': 'ᄅ',
#         'o': 'ᅩ', 't': 'ᄐ',
#         'ō': 'ᅭ', 'w': 'ᄇ',
#         'u': 'ᅮ', 'ŋ': 'ᄉ',
#         'ū': 'ᅲ', 'ƒ': 'ᄌ',
#         'x': 'ᄋ'
#     }

#     decoder_dict = {v: k for k, v in encoder_dict.items()}

#     def __init__(self, vowel_type = 'long'):
#         self.vowel_type = vowel_type

#     def preprocess(self, text, vowel_type):
#         if vowel_type == 'short':
#             text = SingleVowel().encode(text)
#         return text.replace('ng', 'ŋ').replace('wh', 'ƒ')

#     def tokenize(self, text, keep_spaces = False):
#         for i, ch in enumerate(text):
#             if keep_spaces and ch == ' ':
#                 yield ch
#             elif ch == '-':
#                 yield ch
#             elif ch in taumahi.oropuare and text[i-1] not in taumahi.orokati:
#                 # ch is a vowel and the preceding char is not a consonant
#                 yield ch
#             elif ch in taumahi.orokati:
#                 # ch is a consonant
#                 yield text[i:i+2]

#     def encode(self, text):
#         text = self.preprocess(text, vowel_type = self.vowel_type)
#         encoded_sents = []
#         for sent in sent_tokenize(text):
#             sent_encoded = []
#             for syllable in self.tokenize(sent, keep_spaces = True):
#                 if syllable in [" ", "-"]:
#                     sent_encoded.append(syllable)
#                     continue
#                 if len(syllable) == 1:
#                     syllable = 'x' + syllable
#                 try:
#                     consonant, vowel = ''.join([self.encoder_dict[ch] for ch in syllable])
#                 except KeyError:
#                     log.error("KeyError: phoneme {} in sent {} not in encoder_dict".format(syllable, sent))
#                     raise KeyError
#                 try:
#                     encoded = jamo.j2h(consonant, vowel)
#                 except jamo.InvalidJamoError:
#                     log.error('InvalidJamoError - Consonant={} Vowel={} Syllable={} Sent={}'.format(consonant, vowel, syllable, sent[:100]))
#                 sent_encoded.append(encoded)
#             encoded_sents.append(''.join(sent_encoded))
#         return '\n'.join(encoded_sents)

#     def decode(self, encoded_text):
#         decoded_sents = []
#         for sent in sent_tokenize(encoded_text):
#             decoded_sent = ''
#             for ch in sent:
#                 if jamo.is_hangul_char(ch):
#                     decoded_sent += ''.join([self.decoder_dict[ch] for ch in jamo.hangul_to_jamo(ch)])
#                 else:
#                     decoded_sent += ch
#             decoded_sent = decoded_sent.replace('x', '').replace('ŋ', 'ng').replace('ƒ', 'wh')
#             decoded_sents.append(decoded_sent)
#         return '\n'.join(decoded_sents)


# class DoubleVowel:

#     def __init__(self):
#         self.encoder_dict = json.load(open('scripts/double_vowel.json', 'r'), object_pairs_hook=OrderedDict)
#         self.decoder_dict = {v:k for k,v in self.encoder_dict.items()}

#     def encode(self, text):
#         for syllable in self.encoder_dict:
#             text = text.replace(syllable, self.encoder_dict[syllable])
#         return text

#     def decode(self, encoded):
#         lines = []
#         for line in encoded.split('\n'):
#             lines.append(Base().decode(''.join([self.decoder_dict[ch] for ch in line])))
#         return '\n'.join(lines)


# class LongSyllable:

#     def __init__(self):
#         self.encoder_dict = json.load(open('scripts/long_syllable.json', 'r'), object_pairs_hook=OrderedDict)
#         self.decoder_dict = {v:k for k,v in self.encoder_dict.items()}

#     def encode(self, text):
#         for syllable in self.encoder_dict:
#             text = text.replace(syllable, self.encoder_dict[syllable])
#         return text

#     def decode(self, encoded):
#         lines = []
#         for line in encoded.split('\n'):
#             lines.append(Base().decode(''.join([self.decoder_dict[ch] for ch in line])))
#         return '\n'.join(lines)
