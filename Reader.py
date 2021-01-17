import csv


def read_data(filename):
    with open(filename, 'r') as file:
        for row in csv.reader(file):
            yield row
