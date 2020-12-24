from PersonBuilder import PersonBuilder


class DinnerPaymentAlgorithm:

    def __init__(self):
        self.persons = [p for p in PersonBuilder().generate_person()]

        for p in self.persons:
            print(p)

    def calcule_transactions(self):

        print_change_taking()

        creditors, debtors = [], []

        for p in self.persons:
            
            if p.debt > 0:
                debtors += [p]

            elif p.debt < 0:
                creditors += [p]


        for d in debtors:
            for c in creditors:

                if debtor_give_all(d, c) and d.debt * c.debt < 0:
                    print_money_giving(d.name, abs(c.debt), c.name)
                    d.debt, c.debt = transaction(d.debt, c.debt)

                elif creditor_gets_all(d, c) and d.debt * c.debt < 0:
                    print_money_giving(d.name, d.debt, c.name)
                    c.debt, d.debt = transaction(d.debt, c.debt)


def print_change_taking():
    for p in self.persons:
        print(p.name + " takes " + str(p.change) + " from the change.")


def debtor_give_all(d, c):
    return d.debt > abs(c.debt)


def creditor_gets_all(d, c):
    return d.debt < abs(c.debt)


def print_money_giving(issuer, quantity, receiver):
    print(issuer + ' gives ' + str(quantity) + ' to ' + receiver)


def transaction(q1, q2):
    return round(q1 + q2, 2), 0

