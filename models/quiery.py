#!/usr/bin/python3
""" module for the implementation of the quiery """
from models.text import stemmer, tokenizer


class SearchQuiery:
    """ SearchQuiery: is the representation of quiery. """
    def __init__(self, search_queiry: str, index_terms: list) -> None:
        """ Constructor : for the class """
        self.query = search_queiry
        self.query_term_list = tokenizer(search_queiry)
        self.query_term_list_stemmed = [stemmer(term) for term in self.query_term_list ]
        self.term_list_weight = [self.query_term_list.count(term) for term in index_terms ]
        self.stemmed_term_weight = [self.query_term_list_stemmed.count(term) for term in index_terms ]

    def get_weight_list(self):
        """ function to get the weight list """
        print(self.stemmed_term_weight)  
        return self.stemmed_term_weight
