# assumptions 
# I will have this kind of structure
# {'list_of_idx_term: [list of term],
#  'file1.txt': [document matrix reprn]

from models.helpers import load_obj, read_from_file, write_obj
from models.text_operations import tokenizer


document_set = set(['static/files/file1.txt', 'static/files/file2.txt', 'static/files/file3.txt', 'static/files/file4.txt',
                   'static/files/file5.txt', 'static/files/file6.txt'
                   ])
stemmed_term_relationship = load_obj('prog_data/stemmed_terms.json')
term_with_stem = stemmed_term_relationship['term_with_stem']
stem_with_freq = stemmed_term_relationship['stem_with_freq']
stem_with_term = stemmed_term_relationship['stem_with_term']

def get_matrix_repr(serach_quiery):
    text_list = tokenizer(serach_quiery)
    matrix_repr = []

    for stem in sorted(stem_with_freq.keys()):
        res = 0
        for orig_term in stem_with_term[stem]:
            res += text_list.count(orig_term)
        matrix_repr.append(res)
    
    return matrix_repr


def create_inverted_idx_file():
    # create the inverted_idx_file
    inverted_idx_file = {}

    list_of_idx_terms = stem_with_freq.keys()
    list_of_idx_terms = sorted(list_of_idx_terms)

    inverted_idx_file['list_of_idx_term'] = list_of_idx_terms
    inverted_idx_file['files'] = {}

    for file in document_set:
        text = read_from_file(file)
        text_list = tokenizer(text)

        document_matrix = []

        for stemmed_term in list_of_idx_terms:
            res = 0
            for original_term in stem_with_term[stemmed_term]:
                res += text_list.count(original_term)
            document_matrix.append(res)
        
        inverted_idx_file['files'][file] = document_matrix
    

    write_obj('prog_data/inverted_idx_file.json', inverted_idx_file)

if __name__ == '__main__':
    create_inverted_idx_file()