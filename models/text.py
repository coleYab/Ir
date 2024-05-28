import re
from stemmer import stem


def tokenizer(text: str) -> list:
    """ returns after splitting and replacing other chars """
    return re.sub(r'[^\u1200-\u1357\s]|[\u12d7]', '', text).split()

def stopword_remover(text_list: list, removing_factor: float) -> list:
    """ does the stop word removal for the project
    takes: text list and removing factor
    it removes the top removing_factor % and the least removing factor % of the terms.
    """
    text_list_size = len(text_list)
    return text_list[
        int(text_list_size * removing_factor): int(text_list_size - text_list_size * removing_factor)
        ]

def stemmer(word: str) -> str:
    """ a simple porter stemmer with some weakness it doesn't work properly.
    NB: It will not remove infixes in amharic languages, the translitrator
    may have some errors while returning the representation from english to
    amharic for some reasons.
    """
    return stem(word)
