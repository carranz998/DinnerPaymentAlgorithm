from Consumer import Consumer
from Counts import pay_debts, take_change
from Reader import read_data

consumers = [Consumer(name, float(consumed), float(paid))
             for name, consumed, paid in read_data('data.csv')]

actions = [a for a in take_change(consumers)] + [a for a in pay_debts(consumers)]

for a in actions:
    print(a)
