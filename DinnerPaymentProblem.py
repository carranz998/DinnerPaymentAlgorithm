from Person import Person

import pandas as pd


class DinnerPaymentProblem:

    def __init__(self, csv):
        self.df = pd.read_csv(csv)
        self.persons = []
        self.create_persons()

    def create_persons(self):
        for i in range(len(self.df)):
            name, consumed, paid = self.df.iloc[i].values
            person = Person(name, consumed, paid)
            self.persons.append(person)

    def get_persons(self):
        for person in self.persons:
            print(person)

