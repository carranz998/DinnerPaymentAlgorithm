class Person:

    def __init__(self, name, consumed, paid):
        self.name = name
        self.consumed = consumed
        self.paid = paid
        self.change = 0

    def __str__(self):
        return self.name + " " + str(self.consumed) + " " + str(self.paid) + " " + str(self.change)

    def calcule_change(self, total_consumed, total_paid):
        self.change = (self.paid / total_paid) * (total_paid - total_consumed)   
