from typing import List
from stuff.algos import find_max_chain
from stuff.readnwrite import write_to_file
from stuff.readnwrite import read_csv


def main(list: List[str]):
    list.sort(key=lambda x: len(x))
    dictionary = {}
    return find_max_chain(list, dictionary)


if __name__ == '__main__':
    file = 'input.csv'
    write_to_file(main(read_csv(file)))
    print(main(read_csv(file)))
