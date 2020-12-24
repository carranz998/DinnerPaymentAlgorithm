class Person:

    def __init__(self, name, consumed, paid, change, debt):
        self.name = name
        self.consumed = consumed
        self.paid = paid
        self.change = change
        self.debt = debt


    def __str__(self):
        return ''.join(map(str, self.__dict__.items()))
