from Person import Person

import pandas as pd


class DinnerPaymentProblem:

    def __init__(self, csv):
        self.df = pd.read_csv(csv)
        self.persons = []
        self.create_persons()
        self.consumed = self.calcule_consumed()
        self.paid = self.calcule_paid()
        self.change = self.calcule_change()

    def create_persons(self):
        for i in range(len(self.df)):
            name, consumed, paid = self.df.iloc[i].values
            person = Person(name, consumed, paid)
            self.persons.append(person)

    def get_persons(self):
        for person in self.persons:
            print(person)

    def calcule_consumed(self):
        return sum(p.consumed for p in self.persons)

    def calcule_paid(self):
        return sum(p.paid for p in self.persons)

    def calcule_change(self):
        return self.paid - self.consumed

    def change_per_person(self):
        for p in self.persons:
            p.calcule_change(self.consumed, self.paid)
