from PersonBuilder import PersonBuilder


class DinnerPaymentAlgorithm:

    def __init__(self, persons):
        self.persons = persons

    def calcule_transactions(self):

        print_change_taking(self.persons)

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


def print_change_taking(persons):
    for p in persons:
        print(p.name + " takes " + str(p.change) + " from the change.")


def debtor_give_all(debtor, creditor):
    return debtor.debt > abs(creditor.debt)


def creditor_gets_all(debtor, creditor):
    return debtor.debt < abs(creditor.debt)


def print_money_giving(issuer, quantity, receiver):
    print(issuer + ' gives ' + str(quantity) + ' to ' + receiver)


def transaction(q1, q2):
    return round(q1 + q2, 2), 0

