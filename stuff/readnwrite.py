import csv


def read_csv(file):
    word_list = []
    with open(file) as input_file:
        csv_reader = csv.reader(input_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            word_list.append(row[0])
    return word_list


def write_to_file(result):
    f = open("output.txt", "w+")
    f.write(str(result))
    f.close()
