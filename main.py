from DinnerPaymentAlgorithm import DinnerPaymentAlgorithm
from PersonBuilder import PersonBuilder

persons = [p for p in PersonBuilder().generate_person()]

algorithm = DinnerPaymentAlgorithm(persons)
algorithm.calcule_transactions()
