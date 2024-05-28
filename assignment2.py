""" implementation for the assignment 2
Will: generate stemmed : original_term and 
original_term : stemmed term dictionary to enable user
to proceed to the next tasks
"""
import json

from models.text import stemmer, tokenizer
from models.file import create_files, read_from_all_files

file_name = "stemmed.json"


def generate_stemmed_terms(term_list: list) -> dict:
    stemmed_term_data = {}
    
    for term in set(term_list):
        stemmed_term_data[term] = stemmer(term)

    return stemmed_term_data


def reload() -> dict:
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        write(generate_stemmed_terms(
            tokenizer(read_from_all_files(create_files(None)))
        ))
        reload()


def write(stemmed_words: dict):
    with open(file_name, "w") as file:
        json.dump(stemmed_words, file)


if __name__ == '__main__':
    print(reload())