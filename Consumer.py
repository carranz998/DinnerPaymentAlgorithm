class Consumer:

    def __init__(self, name, consumed, paid):
        self.name = name
        self.consumed = consumed
        self.paid = paid
        self.change = 0
        self.debt = 0
