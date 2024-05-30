"""
Implemetation for text operation of amharic language
methods:
    - tokenizer: tokenizes a text
    - normalizer: normalizes a text
    - stop_word_remover: removes stop words in the list
    - stemmer: stemms a given word

"""
import re
# import hm
from models.helpers import sort_dict


def tokenizer(text: str) -> list:
    """ returns after splitting and replacing other chars """
    return re.sub(r'[^\u1200-\u1357\s]|[\u12d7]', '', text).split()

def stop_word_remover(term_frequencies_, upper_cutoff_pt, lower_cutoff_pt) -> dict:
    """ a function to remove the stop words and return the new term dictionary """
    new_term_frequencies_ = {}

    for key, value in term_frequencies_.items():
        if value in range(lower_cutoff_pt, upper_cutoff_pt):
            new_term_frequencies_[key] = value

    return sort_dict(new_term_frequencies_)


def stemmer(word: str) -> str:
    """ a simple porter stemmer with some weakness it doesn't work properly.
    NB: It will not remove infixes in amharic languages, the translitrator
    may have some errors while returning the representation from english to
    amharic for some reasons.
    """
    # term = hm.anal('a', word)

    # pattern = re.compile(r'<([^<>*])>')

    # if term[0]['pos'] in ('UNK', 'PROPN') or 'seg' not in term[0].keys():
        # return word
    # elif 'seg' in term[0].keys():
        # return pattern.search(term[0]['seg'])
    # elif 'lemma' in term[0].keys() and isinstance(term[0]['lemma'], str):
        # return term[0]['lemma']
    # else:
        # return word

    return word