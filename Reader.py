def read_data(filename):
    with open(filename, 'r') as file:
        header = next(file)

        for line in file:
            words = line.split(',')
            name, consumed, paid = words[0], words[1], words[2][:-1]
            yield name, consumed, paid
