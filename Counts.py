def take_change(consumers):
    total_consumed = sum(c.consumed for c in consumers)
    total_paid = sum(c.paid for c in consumers)
    total_change = total_paid - total_consumed

    for c in consumers:
        c.change = round(total_change * c.paid / total_paid, 2)
        yield c.name + " takes " + str(c.change) + " from the change"


def calcule_debts(consumers):
    for c in consumers:
        c.debt = round(c.consumed - c.paid + c.change, 2)


def split_by_debt(consumers):
    return [c for c in consumers if c.debt < 0], [c for c in consumers if c.debt > 0]


def update_debts(creditor, debtor):
    return sorted([round(debtor.debt + creditor.debt, 2), 0])


def pay_debts(consumers):
    calcule_debts(consumers)
    creditors, debtors = split_by_debt(consumers)
    next_creditor, next_debtor = True, True
    creditor, debtor = None, None

    while creditors or debtors:
        creditor = creditors.pop() if next_creditor else creditor
        debtor = debtors.pop() if next_debtor else debtor

        yield debtor.name + " gives " + str(min(-creditor.debt, debtor.debt)) + " to " + creditor.name

        creditor.debt, debtor.debt = update_debts(creditor, debtor)

        next_creditor = not creditor.debt
        next_debtor = not debtor.debt
