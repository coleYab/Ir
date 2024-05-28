#!/usr/bin/python3
""" file module """
from models.text import stemmer, tokenizer


class File:
    """ class to abstract the file """
    def __init__(self, name: str) -> None:
        self.name = name
        self.terms = tokenizer(self.read_from_file())
        self.stemmed_terms = []
        self.stemmed_weight = []

    def get_weight_list(self, idx_term: dict):
        self.stemmed_terms = [idx_term[term] for term in self.terms]
        self.stemmed_weight = [self.stemmed_terms.count(term) for term in set(self.stemmed_terms)]
        return self.stemmed_weight

    def read_from_file(self) -> str:
        try:
            with open(self.name) as file:
                return file.read()
        except FileNotFoundError:
            return ""               

    @staticmethod
    def add_file(file_dicts: dict, file):
        if file.id not in file_dicts.keys():
            file_dicts[file.id] = file

    @staticmethod
    def remove_file(file_dict: dict, file):
        if file.id in file_dict.keys():
            del file_dict[file.id]


def create_files():
    file_paths = ['file/file1.txt', 'file/file2.txt',
                  'file/file3.txt', 'file/file4.txt',
                  'file/file5.txt', 'file/file6.txt']
    
    try:
        files = [ File(name) for name in file_paths ]
    except:
        return file_paths
    
    return files


def read_from_all_files(files: list):
    """ read text from many files. """
    text = ""

    for file in files:
        if (isinstance(file, File)):
            text += file.read_from_file()
        else:
            try:
                with open(file) as f:
                    text += f.read()
            except:
                pass

    return text
