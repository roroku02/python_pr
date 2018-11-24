import random

set_value = set([])
for i in range(100):
    rand_int = random.randint(0, 100)
    set_value.add(rand_int)
for value in set_value:
    print(value)
