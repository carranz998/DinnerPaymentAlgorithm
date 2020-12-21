class Person:

    def __init__(self, name, consumed, paid):
        self.name = name
        self.consumed = consumed
        self.paid = paid

    def __str__(self):
        return self.name + " " + str(self.consumed) + " " + str(self.paid)
