import random ,itertools

deck= list(itertools.product(range(1,14),["spade","club","heart","diamond"]))

random.shuffle(deck)
print(deck)