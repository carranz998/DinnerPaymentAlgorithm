from Person import Person

import pandas as pd


class Receipt:

    def __init__(self, csv):
        self.df = pd.read_csv(csv)
        self.consumed = self.df['consumed'].sum()
        self.paid = self.df['paid'].sum()
        self.change = self.paid - self.consumed
        self.persons = self.create_persons()

        
    def __str__(self):
        return ''.join(str(p) + '\n' for p in self.persons)
        

    def create_persons(self):

        persons = []

        for _, row in self.df.iterrows():

            name, consumed, paid = row.values
            change, overpaid = self.postcounts(consumed, paid)
        
            person = Person(name, consumed, paid, change, overpaid)

            persons += [person]

        return persons
    

    def postcounts(self, consumed, paid):
        
        change = round((paid / self.paid) * self.change, 2)
        overpaid = round(paid - change - consumed, 2)
        
        return change, overpaid
