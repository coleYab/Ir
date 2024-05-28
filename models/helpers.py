from math import sqrt
from models.file import File
from models.quiery import SearchQuiery
from stemmer import stem


def cosine_simmilarity(file: File, quiery: SearchQuiery) -> float:
    """ Simple calculation for term cosine simmilarity given the choice by the user """

    qweight_list = quiery.get_weight_list()
    fweight_list = file.get_weight_list()

    queiry_magnitude = sqrt(sum(weight ** 2 for weight in qweight_list))
    file_magnitude = sqrt(sum(weight ** 2 for weight in fweight_list))

    dot_product = sum(
        fweight_list[i] * qweight_list[i] for i in range(len(qweight_list))
    )

    return dot_product / queiry_magnitude * file_magnitude


def sort_dict(dictionary: dict):
    """ Helper function to sort a dictionary """
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))


def count_frequency(term_list: list):
    """ returns the count to frequency ratio for the given file """
    frequency_count = {}

    for term in set(term_list):
        frequency_count[term] = term_list.count(term)

    return frequency_count


def calculate_ranks(term_lists: dict):
    """ calculates the rank for the given frequencies. """
    ranks = []
    rank = 1
    prev_score = None
    for score in term_lists:
        if score != prev_score:
            rank += 1
        ranks.append(rank)
        prev_score = score
    return ranks


def search(search_quiery: SearchQuiery, file_lists: list, idx_terms) -> dict:
    """ implements searching of the files in the list """
    results = {}
    final_result = []

    # calculating the cosign simmilarity between files.
    for file in file_lists:
        cos_sim = cosine_simmilarity(File(file, idx_terms), search_quiery)
        if cos_sim > 0:
            results[file] = cos_sim
    results = sort_dict(results)

    # Assuming that they are sorted in descending order
    # we will construct the result inorder to be displayed by flask.
    files = results.keys()
    for i in range(len(files)):
        result_data = {
            "file_name": files[i].name,
            "rank": i + 1,
            "description": files[i].description,
            "simmilarity_val": results[files[i]]
        }
        final_result.append(result_data)

    return final_result
