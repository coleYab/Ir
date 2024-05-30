import json
import matplotlib.pyplot as plt

from models.text_operations import tokenizer
from models.helpers import count_term_frequency as count_frequency, load_obj, read_from_file, sort_dict


def draw_graph(frequency: list) -> None:
    """
    draw_graph: draws graph.
    """
    rank_ = [i for i in range(1, len(frequency) + 1)]
    plt.plot(rank_, sorted(frequency, reverse=True))
    plt.ylabel('Frequency of terms')
    plt.xlabel('Rank of terms')
    plt.title('Frequency - Rank Graph')
    plt.show()


def plot_table(data, column_labels):
    fig, ax = plt.subplots()
    ax.axis("tight")
    plt.rcParams['font.family'] = 'Abyssinica SIL'
    ax.axis("off")
    table = ax.table(cellText=data, colLabels=column_labels, loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)
    plt.show()



def main():
    text_frequency = load_obj('prog_data/term_freq.json')
    draw_graph(text_frequency.values())
    with open('test.json','w') as file:
        json.dump(text_frequency, file)


def main1():
    text = read_from_file('static/files/original.txt')
    text_list = tokenizer(text)
    text_frequency = count_frequency(text_list)
    text_frequency = sort_dict(text_frequency)
    total_words = sum(text_frequency.values())
    data = []
    count = 0

    for word, freq in text_frequency.items():
        count += 1
        percent_occurance = freq / total_words * 100
        data.append(
            [word, freq, count, round(percent_occurance, 2), round(percent_occurance*count, 2)]
        )

    column_labels = ["Word", "Frequency", "Rank", "% of occurance","r*f"]
    plot_table(data[0:10], column_labels)

if __name__ == '__main__':
    # After the end of this stage we will generate a json file that will consists of term in the files
    # and their initial frequencies used in the first term this will be used by second assignment
    main()
