class Person:

    def __init__(self, name, consumed, paid, change, overpaid):
        self.name = name
        self.consumed = consumed
        self.paid = paid
        self.change = change
        self.overpaid = overpaid

    def __str__(self):
        return ''.join(map(str, self.__dict__.items()))
