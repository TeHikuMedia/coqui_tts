# import argparse
# import logging

# import re
# import json
# import taumahi
# import nltk
# import jamo

# from collections import OrderedDict
# from reo_toolkit import is_maori

# # initialise logger
# log = logging.getLogger(__name__)

# # removing all non-alphanumeric characters
# alphanum = re.compile(r'[^A-Za-z0-9āēīōū \-]+', re.UNICODE)
# single_space = re.compile('\s{2,}', re.UNICODE)
# trailing_hyphens = re.compile('\-+[^A-zāēīōūŋƒ]+|[^A-zāēīōūŋƒ]+\-+|^\-+|\-+$')

# def sent_tokenize(text):
#     for para in text.split("\n"):
#         for sent in nltk.sent_tokenize(para):
#             sent = sent.strip()
#             if len(sent) > 0:
#                 yield sent

# def drop_non_maori_words(sent):
#     # Throw out non_maori words from sentence
#     sent_out = []
#     for kupu in sent.split(" "):
#         maori, ambiguous, non_maori = taumahi.kōmiri_kupu(kupu)
#         if len(kupu.replace("-", "")) == 1 and not kupu in taumahi.oropuare:
#             # if kupu is a single character and not a maori vowel
#             continue
#         if re.match('.*[' + taumahi.orokati + ']+\-.*', kupu):
#             # if kupu contains a consonant followed by a hyphen
#             continue
#         if not re.match('[' + taumahi.orokati + taumahi.oropuare + '\-]+', kupu):
#             # if kupu does not contain only maori vowels + consonants + hyphens
#             continue

#         if not non_maori:
#             sent_out.append(kupu)

#     return ' '.join(sent_out)

# def digits_to_text(match):

#     num = int(match.group())

#     if abs(num) >= 10000:
#         # Get rid of large numbers
#         return ''

#     digits = [int(i) for i in str(num)]

#     ones = ['kore', 'tahi', 'rua', 'toru', 'whā',
#             'rima', 'ono', 'whitu', 'waru', 'iwa']
#     places = ['mano', 'rau', 'tekau', '']

#     ones_dict   = dict(zip([i for i in range(10)], ones))
#     places_dict = dict(zip([3, 2, 1, 0], places))

#     digit_words = []
#     for place, digit in enumerate(digits[::-1]):
#         ones_digit = ones_dict[digit]

#         place_digit = places_dict[place]

#         if place == 1:
#             place_digit = place_digit + " mā"

#         if place > 1 and ones_digit == 'tahi':
#             ones_digit = "kotahi"

#         place_words = str.strip(ones_digit + " " + place_digit)

#         digit_words.append(place_words)

#     digit_text = ' '.join(digit_words[::-1])

#     digit_text = str.strip(digit_text
#         .replace(" mā kore", "")
#         .replace(" kore rau", "")
#         .replace("kore tekau ", "")
#         .replace("tahi tekau ", "tekau "))

#     return digit_text

# def fix_numbers(text):
#     return re.sub(r'\d+', digits_to_text, text)


# def clean_text(text):

#     text = text.lower()

#     # replace % symbol with 'paihēneti'
#     text = text.replace('%', ' paihēneti')

#     # remove numbers (for now)
#     text = fix_numbers(text)

#     # remove non-alphanumeric characters
#     text = alphanum.sub(' ', text)

#     text = drop_non_maori_words(text)

#     # ensure only single space
#     text = single_space.sub(' ', text)

#     # remove trailing hyphens
#     text = trailing_hyphens.sub(' ', text)
#     text = re.sub('\-{2,}', '-', text)

#     text = drop_non_maori_words(text)

#     # substitute 'f' for 'wh'
#     text = text.replace("wh", "ƒ")

#     # substitute 'η' for 'ng'
#     text = text.replace("ng", "ŋ")

#     # remove trailing spaces
#     text = text.strip()

#     return text



# def preprocess(text):

#     clean_sents = []
#     for sent in sent_tokenize(text):
#         sent = clean_text(sent)
#         clean_sents.append(sent)

#     clean_texts = "\n".join([sent for sent in clean_sents if is_maori(sent, strict = True)])

#     return clean_texts


