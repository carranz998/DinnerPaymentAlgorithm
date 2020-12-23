from PersonBuilder import PersonBuilder


class DinnerPaymentAlgorithm:

    def __init__(self):
        self.persons = [p for p in PersonBuilder().generate_person()]

