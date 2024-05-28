import matplotlib.pyplot as plt

from models.file import File, read_from_all_files
from models.helpers import calculate_ranks, count_frequency, sort_dict
from models.text import tokenizer


def draw_graph(frequency: list) -> None:
    """
    draw_graph: draws graph.
    """
    rank_ = calculate_ranks(frequency)
    plt.plot(rank_, frequency)
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
    paths = ['file/file1.txt', 'file/file2.txt', 'file/file3.txt']
    files = [ File(name, set()) for name in paths ]
    print(files)
    text = read_from_all_files(files)
    text_list = tokenizer(text)
    text_frequency = count_frequency(text_list)
    text_frequency = sort_dict(text_frequency)
    draw_graph(text_frequency.values())


def main1():
    paths = ['file/file1.txt', 'file/file2.txt', 'file/file3.txt']    
    files = [ File(name, set()) for name in paths ]
    text = read_from_all_files(files)
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

    column_labels = ["Word", "Frequency", "Rank", "% occurance","r*f"]
    plot_table(data[0:10], column_labels)

if __name__ == '__main__':
    main()