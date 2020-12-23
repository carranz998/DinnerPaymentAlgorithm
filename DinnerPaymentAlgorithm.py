from PersonBuilder import PersonBuilder


class DinnerPaymentAlgorithm:

    def __init__(self):
        self.persons = [p for p in PersonBuilder().generate_person()]

        for p in self.persons:
            print(p)
