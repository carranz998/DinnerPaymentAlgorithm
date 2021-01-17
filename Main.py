from Counts import take_change, pay_debts
from Consumer import Consumer
from Reader import read_data

actors = [Consumer(name, float(consumed), float(paid))
          for name, consumed, paid in read_data('data.csv')]

for action in take_change(actors) + pay_debts(actors):
    print(action)
