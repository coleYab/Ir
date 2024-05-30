from models.inverted_idx import get_matrix_repr
from models.helpers import search, build_result

if __name__ == '__main__':
    search_q = str(input("Enter your quiery: "))
    print(build_result(search(search_q, get_matrix_repr)))