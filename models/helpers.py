import json
import math


def load_obj(file_path: str) -> dict:
    try:
        with open(file_path) as file:
            return json.load(file)
    except FileNotFoundError:
        pass
    return {}


def write_obj(file_path: str, item) -> None:
    with open(file_path, 'w') as file:
        json.dump(item, file)


def count_term_frequency(term_list: list) -> dict:
    term_frequency = {}

    with open('prog_data/term_freq.json', 'w') as file:
        for term in set(term_list):
            term_frequency[term] = term_list.count(term)
        json.dump(term_frequency, file)
    
    return term_frequency


def read_from_file(file_path: str) -> str:
    try:
        with open(file_path) as file:
            return file.read()
    except:
        print('Pussio I am here')
        return ""    

def sort_dict(dictionary: dict):
    """ Helper function to sort a dictionary """
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))


def cosine_simmilarity(mat1, mat2):
    mat1_mag = math.sqrt(sum(i ** 2 for i in mat1))
    mat2_mag = math.sqrt(sum(i ** 2 for i in mat2))

    dot_prod = sum(mat1[i] * mat2[i] for i in range(len(mat1)))

    return dot_prod / (mat1_mag * mat2_mag)

def search(serach_quiery, get_matrix_repr):
    """ implementation of the search engine """
    result = {}

    matq = get_matrix_repr(serach_quiery)
    idx_structure = load_obj('prog_data/inverted_idx_file.json')

    for file, matrix in idx_structure['files'].items():
        cos_sim = cosine_simmilarity(matq, idx_structure['files'][file])
        if cos_sim > 0:
            result[file] = cos_sim

    return sort_dict(result)


def build_result(result_from_search):
    results = []
    count = 1

    for file, cos_sim in result_from_search.items():
        res_data = {}
        res_data['file_name'] = file.replace('static/files/', '')
        res_data['file_path'] = file.replace('static/', '')
        res_data['cos_sim'] = cos_sim
        res_data['rank'] = count
        count += 1
        results.append(res_data)

    return results

if __name__ == '__main__':
    search_quiery = str(input("Enter your serach quiery: "))
