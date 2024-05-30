from models.text_operations import stemmer, stop_word_remover
from models.helpers import load_obj, write_obj

def main():
    term_frequency_ = load_obj('prog_data/term_freq.json')
    term_frequency_ = stop_word_remover(term_frequency_, 900, 20)
    
    # lets build the stemmed terms structures
    # we will create a key: value relationship with the original term 
    # and the stemmed term
    stemmed_term_relationship = {}
    stemmed_term_freq = {}
    stem_with_terms = {}
    original_term_w_stemmed_term = {}
    counter = 0

    for term, freq in term_frequency_.items():
        stem_of_term = stemmer(term)

        print(counter, end="---------------\n\n")
        counter += 1

        # taking care of the stemmed term frequency
        if stem_of_term in stemmed_term_freq.keys():
            stemmed_term_freq[stem_of_term] += freq
        else:
            stemmed_term_freq[stem_of_term] = freq

        # adding the stemmed term to the original term mapping
        # this will be usefull when constructing idf later
        if stem_of_term not in stem_with_terms.keys():
            stem_with_terms[stem_of_term] = [term]
        else:
            stem_with_terms[stem_of_term].append(term)
        
        # taking care of the original term and the stemmed term
        original_term_w_stemmed_term[term] = stem_of_term
        
        # now we will write the result of the stemming to the json file.
        stemmed_term_relationship['term_with_stem'] = original_term_w_stemmed_term
        stemmed_term_relationship['stem_with_freq'] = stemmed_term_freq
        stemmed_term_relationship['stem_with_term'] = stem_with_terms

        write_obj('prog_data/stemmed_terms.json', stemmed_term_relationship)

    print(stemmed_term_relationship)

if __name__ == '__main__':
    main()