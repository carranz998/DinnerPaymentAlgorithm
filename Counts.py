def take_change(consumers):

    total_consumed = sum(c.consumed for c in consumers)
    total_paid = sum(c.paid for c in consumers)

    total_change = total_paid - total_consumed

    actions = []

    for c in consumers:
        c.change = round(total_change * c.paid / total_paid, 2)
        actions.append(c.name + " takes " + str(c.change) + " from the change")

    return actions


def calcule_debts(consumers):
    for c in consumers:
        c.debt = round(c.consumed - c.paid + c.change, 2)


def pay_debts(consumers):

    calcule_debts(consumers)

    creditors = [c for c in consumers if c.debt < 0]
    debtors = [c for c in consumers if c.debt > 0]

    next_creditor, next_debtor = True, True
    creditor, debtor = None, None
    actions = []

    while creditors or debtors:
        creditor = creditors.pop() if next_creditor else creditor
        debtor = debtors.pop() if next_debtor else debtor

        actions.append(debtor.name + " gives " + str(min(-creditor.debt, debtor.debt)) + " to " + creditor.name)

        creditor.debt, debtor.debt = sorted([round(debtor.debt + creditor.debt, 2), 0])

        next_creditor = not creditor.debt
        next_debtor = not debtor.debt

    return actions
