from Person import Person

import pandas as pd


class DinnerPaymentAlgorithm:

    def __init__(self, csv):
        self.df = pd.read_csv(csv)
        self.consumed = self.df['consumed'].sum()
        self.paid = self.df['paid'].sum()
        self.change = self.paid - self.consumed
        self.persons = self.create_persons()

        for p in self.persons:
            print(p)

    def __str__(self):
        return ''.join(map(str, self.__dict__.items()))


    def create_persons(self):

        persons = []
        
        for _, row in self.df.iterrows():
                        
            name, consumed, paid = row.values
            change = (paid / self.paid) * self.change
            overpaid = paid - change - consumed
            
            persons += [Person(name, consumed, paid, change, overpaid)]

        return persons
